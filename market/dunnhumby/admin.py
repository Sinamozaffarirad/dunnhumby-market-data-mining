from django.contrib import admin
from django.db.models import Sum, Count, Avg, Max
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.utils.html import format_html
from .models import (
    Transaction, DunnhumbyProduct, Household, Campaign, Coupon,
    CouponRedemption, CampaignMember, CausalData, BasketAnalysis,
    AssociationRule, CustomerSegment
)
import json
from collections import defaultdict


class DunnhumbyAdminSite(admin.AdminSite):
    site_header = "Dunnhumby Market Analysis Admin"
    site_title = "Market Analysis"
    index_title = "Shopping Basket Analysis & Database Management"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('basket-analysis/', self.admin_view(self.basket_analysis_view), name='basket-analysis'),
            path('association-rules/', self.admin_view(self.association_rules_view), name='association-rules'),
            path('customer-segments/', self.admin_view(self.customer_segments_view), name='customer-segments'),
            path('data-manipulation/', self.admin_view(self.data_manipulation_view), name='data-manipulation'),
        ]
        return custom_urls + urls

    def index(self, request, extra_context=None):
        """Custom admin index page with analysis tools"""
        extra_context = extra_context or {}
        
        # Add custom analysis tools to the context
        extra_context['analysis_tools'] = [
            {
                'title': 'Shopping Basket Analysis',
                'description': 'Analyze shopping baskets, top products, and purchasing patterns',
                'url': 'basket-analysis/',
                'icon': '📊'
            },
            {
                'title': 'Association Rules Mining',
                'description': 'Generate and view market basket association rules',
                'url': 'association-rules/',
                'icon': '🔗'
            },
            {
                'title': 'Customer Segmentation',
                'description': 'RFM analysis and customer behavioral segments',
                'url': 'customer-segments/',
                'icon': '👥'
            },
            {
                'title': 'Data Manipulation',
                'description': 'Database management and analysis data refresh tools',
                'url': 'data-manipulation/',
                'icon': '⚙️'
            }
        ]
        
        return super().index(request, extra_context)

    def basket_analysis_view(self, request):
        """Shopping basket analysis dashboard"""
        # Get basket statistics
        basket_stats = Transaction.objects.values('basket_id').annotate(
            total_items=Sum('quantity'),
            total_value=Sum('sales_value'),
            unique_products=Count('product_id', distinct=True)
        ).order_by('-total_value')[:20]

        # Department analysis
        dept_analysis = Transaction.objects.values(
            'product_id'
        ).annotate(
            total_sales=Sum('sales_value'),
            total_transactions=Count('product_id')
        ).order_by('-total_sales')[:10]

        # Top products by frequency
        top_products = Transaction.objects.values(
            'product_id'
        ).annotate(
            frequency=Count('product_id'),
            total_sales=Sum('sales_value')
        ).order_by('-frequency')[:20]

        context = {
            'title': 'Shopping Basket Analysis',
            'basket_stats': basket_stats,
            'dept_analysis': dept_analysis,
            'top_products': top_products,
        }
        return TemplateResponse(request, 'admin/dunnhumby/basket_analysis.html', context)

    def association_rules_view(self, request):
        """Association rules analysis"""
        if request.method == 'POST':
            min_support = float(request.POST.get('min_support', 0.01))
            min_confidence = float(request.POST.get('min_confidence', 0.5))
            
            # Generate association rules (simplified implementation)
            rules = self.generate_association_rules(min_support, min_confidence)
            
            context = {
                'title': 'Association Rules',
                'rules': rules,
                'min_support': min_support,
                'min_confidence': min_confidence,
            }
        else:
            context = {
                'title': 'Association Rules',
                'rules': AssociationRule.objects.all().order_by('-lift')[:50],
            }
        
        return TemplateResponse(request, 'admin/dunnhumby/association_rules.html', context)

    def customer_segments_view(self, request):
        """Customer segmentation dashboard"""
        # RFM Analysis summary
        segments = CustomerSegment.objects.values('rfm_segment').annotate(
            count=Count('household_key'),
            avg_spend=Avg('total_spend'),
            avg_transactions=Avg('total_transactions')
        ).order_by('-count')

        # Recent customer analysis
        recent_customers = CustomerSegment.objects.order_by('-updated_at')[:20]

        context = {
            'title': 'Customer Segmentation',
            'segments': segments,
            'recent_customers': recent_customers,
        }
        return TemplateResponse(request, 'admin/dunnhumby/customer_segments.html', context)

    def data_manipulation_view(self, request):
        """Database manipulation interface"""
        if request.method == 'POST':
            action = request.POST.get('action')
            result_message = ""
            
            if action == 'refresh_basket_analysis':
                # Refresh basket analysis data
                self.refresh_basket_analysis()
                result_message = "Basket analysis refreshed successfully"
            elif action == 'generate_segments':
                # Generate RFM segments
                self.generate_rfm_segments()
                result_message = "Customer segments generated successfully"
            elif action == 'clean_data':
                # Clean inconsistent data
                cleaned = self.clean_data()
                result_message = f"Data cleaning completed. {cleaned} records processed"
            
            context = {
                'title': 'Database Manipulation',
                'result_message': result_message,
                'data_stats': self.get_data_statistics(),
            }
        else:
            context = {
                'title': 'Database Manipulation',
                'data_stats': self.get_data_statistics(),
            }
        
        return TemplateResponse(request, 'admin/dunnhumby/data_manipulation.html', context)

    def generate_association_rules(self, min_support, min_confidence):
        """Generate association rules (simplified)"""
        # This is a simplified implementation
        # In production, you'd use libraries like mlxtend or apyori
        
        # Get frequent itemsets using values() to avoid 'id' column issue
        baskets = defaultdict(list)
        transactions = Transaction.objects.values('basket_id', 'product_id')[:10000]  # Limit for demo
        for transaction in transactions:
            baskets[transaction['basket_id']].append(str(transaction['product_id']))
        
        # Simple frequent pairs analysis
        pair_counts = defaultdict(int)
        total_baskets = len(baskets)
        
        for basket_items in baskets.values():
            for i in range(len(basket_items)):
                for j in range(i+1, len(basket_items)):
                    pair = tuple(sorted([basket_items[i], basket_items[j]]))
                    pair_counts[pair] += 1
        
        # Generate rules
        rules = []
        for pair, count in pair_counts.items():
            support = count / total_baskets
            if support >= min_support:
                # Calculate confidence (simplified)
                antecedent_count = sum(1 for basket_items in baskets.values() if pair[0] in basket_items)
                confidence = count / antecedent_count if antecedent_count > 0 else 0
                
                if confidence >= min_confidence:
                    consequent_count = sum(1 for basket_items in baskets.values() if pair[1] in basket_items)
                    lift = confidence / (consequent_count / total_baskets) if consequent_count > 0 else 0
                    
                    rules.append({
                        'antecedent': [pair[0]],
                        'consequent': [pair[1]],
                        'support': support,
                        'confidence': confidence,
                        'lift': lift
                    })
        
        return sorted(rules, key=lambda x: x['lift'], reverse=True)[:20]

    def refresh_basket_analysis(self):
        """Refresh basket analysis data"""
        BasketAnalysis.objects.all().delete()
        
        baskets = Transaction.objects.values('basket_id', 'household_key').annotate(
            total_items=Sum('quantity'),
            total_value=Sum('sales_value')
        )
        
        for basket in baskets[:1000]:  # Limit for demo
            BasketAnalysis.objects.update_or_create(
                basket_id=basket['basket_id'],
                defaults={
                    'household_key': basket['household_key'],
                    'total_items': basket['total_items'] or 0,
                    'total_value': basket['total_value'] or 0,
                    'department_mix': {}
                }
            )

    def generate_rfm_segments(self):
        """Generate RFM customer segments"""
        # This would implement proper RFM analysis
        # For now, simplified implementation
        try:
            customers = Transaction.objects.values('household_key').annotate(
                last_transaction=Max('day'),
                total_transactions=Count('basket_id'),
                total_spend=Sum('sales_value'),
                avg_basket_value=Avg('sales_value')
            )
            
            # Use truncate to safely clear all records
            CustomerSegment.objects.all().delete()
        except Exception as e:
            # Log error and continue with update_or_create approach
            print(f"Error in RFM segments: {e}")
            return
        
        for customer in customers[:1000]:  # Limit for demo
            try:
                # Simplified RFM scoring (1-5 scale)
                recency_score = min(5, max(1, int((400 - customer['last_transaction']) / 80)))
                frequency_score = min(5, max(1, int(customer['total_transactions'] / 20)))
                monetary_score = min(5, max(1, int(customer['total_spend'] / 100)))
                
                # Determine segment based on scores
                if recency_score >= 4 and frequency_score >= 4 and monetary_score >= 4:
                    segment = "Champions"
                elif recency_score >= 3 and frequency_score >= 3:
                    segment = "Loyal Customers"
                elif recency_score >= 4:
                    segment = "New Customers"
                elif monetary_score >= 4:
                    segment = "Big Spenders"
                elif frequency_score >= 4:
                    segment = "Regular Customers"
                elif recency_score <= 2:
                    segment = "At Risk"
                else:
                    segment = "Standard"
                
                CustomerSegment.objects.update_or_create(
                    household_key=customer['household_key'],
                    defaults={
                        'recency_score': recency_score,
                        'frequency_score': frequency_score,
                        'monetary_score': monetary_score,
                        'rfm_segment': segment,
                        'last_transaction_day': customer['last_transaction'],
                        'total_transactions': customer['total_transactions'],
                        'total_spend': customer['total_spend'],
                        'avg_basket_value': customer['avg_basket_value']
                    }
                )
            except Exception as e:
                # Skip this customer if there's an error
                print(f"Skipping customer {customer['household_key']}: {e}")
                continue

    def clean_data(self):
        """Clean inconsistent data"""
        # Remove transactions with invalid values (using raw SQL to avoid 'id' column issue)
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("UPDATE transactions SET sales_value = 0 WHERE sales_value < 0")
            cleaned = cursor.rowcount
        
        return cleaned

    def get_data_statistics(self):
        """Get current data statistics"""
        return {
            'total_transactions': Transaction.objects.count(),
            'total_products': DunnhumbyProduct.objects.count(),
            'total_households': Household.objects.count(),
            'total_campaigns': Campaign.objects.count(),
            'basket_analyses': BasketAnalysis.objects.count(),
            'association_rules': AssociationRule.objects.count(),
            'customer_segments': CustomerSegment.objects.count(),
        }


# Create custom admin site instance
dunnhumby_admin_site = DunnhumbyAdminSite(name='dunnhumby_admin')


# Transaction model removed from admin due to lack of primary key
# Use custom views in the admin site instead
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('basket_id', 'household_key', 'product_id', 'quantity', 'sales_value', 'day')
    list_filter = ('day', 'week_no', 'store_id')
    search_fields = ('basket_id', 'household_key', 'product_id')
    list_per_page = 50
    ordering = ('-day', '-basket_id')


@admin.register(DunnhumbyProduct)
class DunnhumbyProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'commodity_desc', 'brand', 'department', 'manufacturer')
    list_filter = ('department', 'brand', 'manufacturer')
    search_fields = ('commodity_desc', 'sub_commodity_desc', 'brand')
    list_per_page = 50


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('household_key', 'age_desc', 'income_desc', 'homeowner_desc', 'hh_comp_desc')
    list_filter = ('age_desc', 'income_desc', 'homeowner_desc')
    search_fields = ('household_key',)


@admin.register(BasketAnalysis)
class BasketAnalysisAdmin(admin.ModelAdmin):
    list_display = ('basket_id', 'household_key', 'total_items', 'total_value', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('basket_id', 'household_key')
    readonly_fields = ('department_mix',)


@admin.register(AssociationRule)
class AssociationRuleAdmin(admin.ModelAdmin):
    list_display = ('get_rule_display', 'support', 'confidence', 'lift', 'rule_type', 'created_at')
    list_filter = ('rule_type', 'created_at')
    ordering = ('-lift', '-confidence')
    
    def get_rule_display(self, obj):
        ant = ', '.join(map(str, obj.antecedent))
        con = ', '.join(map(str, obj.consequent))
        return f"{ant} → {con}"
    get_rule_display.short_description = "Rule"


@admin.register(CustomerSegment)
class CustomerSegmentAdmin(admin.ModelAdmin):
    list_display = ('household_key', 'rfm_segment', 'recency_score', 'frequency_score', 
                   'monetary_score', 'total_spend', 'updated_at')
    list_filter = ('rfm_segment', 'recency_score', 'frequency_score', 'monetary_score')
    search_fields = ('household_key',)
    ordering = ('-total_spend',)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'description', 'start_day', 'end_day')
    list_filter = ('description',)
    ordering = ('campaign',)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_upc', 'product_id', 'campaign')
    list_filter = ('campaign',)
    search_fields = ('coupon_upc', 'product_id')


# CouponRedemption model removed from admin due to lack of primary key
class CouponRedemptionAdmin(admin.ModelAdmin):
    list_display = ('household_key', 'coupon_upc', 'campaign', 'day')
    list_filter = ('campaign', 'day')
    search_fields = ('household_key', 'coupon_upc')


# Register models with the custom admin site (excluding models without proper primary keys)
# dunnhumby_admin_site.register(Transaction, TransactionAdmin)  # Commented out - no primary key
dunnhumby_admin_site.register(DunnhumbyProduct, DunnhumbyProductAdmin)
dunnhumby_admin_site.register(Household, HouseholdAdmin)
dunnhumby_admin_site.register(Campaign, CampaignAdmin)
dunnhumby_admin_site.register(BasketAnalysis, BasketAnalysisAdmin)
dunnhumby_admin_site.register(AssociationRule, AssociationRuleAdmin)
dunnhumby_admin_site.register(CustomerSegment, CustomerSegmentAdmin)
