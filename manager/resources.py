from import_export import resources
from import_export.fields import Field
from . import models


class CustomerResource(resources.ModelResource):
    class Meta:
        model = models.Customer
        fields = ('title', 'kind', 'inn', 'email', 'address', 'phone')


class OrderResource(resources.ModelResource):
    customer = Field(attribute='customer__title')

    class Meta:
        model = models.Order
        fields = ('created', 'ended', 'customer', 'is_active', 'priority', 'text')


class ResourceResource(resources.ModelResource):
    class Meta:
        model = models.Resource
        fields = ('title', 'order', 'unit', 'email', 'quantity', 'cost', 'total')


class EquipmentResource(resources.ModelResource):
    class Meta:
        model = models.Equipment
        fields = ('title', 'sector', 'serial', 'code', 'cost')


class SectorResource(resources.ModelResource):
    class Meta:
        model = models.Sector
        fields = ('title', 'order', 'manager',)


class TechnicalProcessResource(resources.ModelResource):
    booking = Field(attribute='booking__title')
    sector_name = Field(attribute='sector__title')

    class Meta:
        model = models.TechnicalProcess
        fields = ('title', 'order', 'booking' 'text', 'sector_name', 'form')
