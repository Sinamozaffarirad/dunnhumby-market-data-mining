from django.urls import path
from . import views

app_name = "dunnhumby_site"

urlpatterns = [
    path("", views.site_index, name="index"),
    path("basket-analysis/", views.basket_analysis, name="basket_analysis"),
    path("association-rules/", views.association_rules, name="association_rules"),
    path("customer-segments/", views.customer_segments, name="customer_segments"),
    path("data-management/", views.data_management, name="data_management"),
    # JSON/API endpoints used by front-end JS
    path("api/table/", views.api_get_table_data, name="api_get_table_data"),
    path("api/update/", views.api_update_record, name="api_update_record"),
    path("api/export/", views.api_export_data, name="api_export_data"),
    path("api/schema/", views.api_table_schema, name="api_table_schema"),
]
