from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, CustomerProfile

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    # if you want to tweak which fields show up, you can override fieldsets,
    # list_display, search_fields, etc. For now the default is fine.
    pass

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display  = ("user", "joined_at", "spend_90d", "churn_score")
    search_fields = ("user__username", "user__email")
    list_filter   = ("joined_at",)
