from import_export import resources
from import_export.fields import Field
from . import models


class CustomerResource(resources.ModelResource):
    title = Field(attribute='title')
    type_of_organization = Field(attribute='get_kind_display')

    class Meta:
        model = models.Customer
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        fields = ('title', 'type_of_organization', 'inn', 'email', 'address', 'phone')


class OrderResource(resources.ModelResource):
    customer_id = Field(attribute='customer__id')

    class Meta:
        model = models.Order
        skip_unchanged = True                # Пропускаем не измененные записи
        report_skipped = True                # Предупреждаем о скипнутых записях
        exclude = ('id',)                    # Автоинкрементируемое поле - его исключаем из выгрузки
        import_id_fields = ('customer_id',)  # Поля, которые имеют тип данных ForeignKey
        fields = ('created', 'ended', 'customer_id', 'is_active', 'priority', 'text')


class ResourceResource(resources.ModelResource):
    class Meta:
        model = models.Resource
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        fields = ('title', 'order', 'unit', 'email', 'quantity', 'cost', 'total')


class EquipmentResource(resources.ModelResource):
    sector_id = Field(attribute='sector__id')

    class Meta:
        model = models.Equipment
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('sector_id',)
        fields = ('title', 'sector', 'serial', 'code', 'cost')


class SectorResource(resources.ModelResource):
    class Meta:
        model = models.Sector
        fields = ('title', 'order', 'manager',)


class TechnicalProcessResource(resources.ModelResource):
    client = Field(attribute='booking__customer__title')
    sector_name = Field(attribute='sector__title')
    form = Field(attribute='get_form_display')

    class Meta:
        model = models.TechnicalProcess
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        fields = ('title', 'order', 'client' 'text', 'sector_name', 'form')
