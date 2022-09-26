from distutils import core
from django.contrib import admin
from tenants.utils import tenant_from_request, set_tenant_schema_for_request
from .models import Prospect


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    fields = ["name", "email", "added_by","join_date"]
    readonly_fields = ["join_date"]

    def get_queryset(self, request, *args, **kwargs):
        set_tenant_schema_for_request(self.request) #
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        set_tenant_schema_for_request(self.request) #
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)