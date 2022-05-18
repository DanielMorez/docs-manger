from django.contrib import admin

from . import models
from . import resources

from nested_admin.nested import NestedModelAdmin, NestedStackedInline
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin


class EquipmentInline(NestedStackedInline):
    model = models.Equipment
    extra = 0


@admin.register(models.Sector)
class SectorAdmin(NestedModelAdmin, ExportActionModelAdmin):
    list_display = ('title', 'order', 'manager',)
    search_fields = ('title', 'manager')
    inlines = (EquipmentInline,)
    resource_class = resources.SectorResource


@admin.register(models.Customer)
class CustomerAdmin(ExportActionModelAdmin):
    list_display = ('title', 'kind', 'inn', 'email', 'address', 'phone',)
    search_fields = ('title', 'inn', 'email', 'address', 'phone')
    list_filter = ('kind',)
    resource_class = resources.CustomerResource


@admin.register(models.Resource)
class ResourceAdmin(ExportActionModelAdmin):
    list_display = ('title', 'order', 'unit', 'quantity', 'cost', 'total',)
    resource_class = resources.ResourceResource


@admin.register(models.Equipment)
class EquipmentAdmin(ExportActionModelAdmin):
    list_display = ('title', 'sector', 'serial', 'code', 'cost',)
    resource_class = resources.EquipmentResource


class ResourceInline(NestedStackedInline):
    model = models.Resource
    extra = 0


class TechnicalProcessInline(NestedStackedInline):
    model = models.TechnicalProcess
    extra = 0


@admin.register(models.Order)
class OrderAdmin(NestedModelAdmin, ExportActionModelAdmin):
    list_display = ('created', 'customer', 'ended', 'is_active', 'priority', 'text')
    list_editable = ('is_active',)
    search_fields = ('customer', 'text', 'created', 'ended')
    list_filter = ('is_active', 'priority')
    inlines = (ResourceInline, TechnicalProcessInline,)
    resource_class = resources.OrderResource


@admin.register(models.TechnicalProcess)
class TechnicalProcessAdmin(ExportActionModelAdmin):
    list_display = ('title', 'booking', 'order', 'sector', 'text', 'form')
    search_fields = ('title', 'form'),
    list_filter = ('sector',)
    resource_class = resources.TechnicalProcessResource
