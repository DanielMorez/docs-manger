from manager.models import Order, Customer, Equipment, Sector, Resource
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('created', 'ended', 'customer', 'is_active', 'priority', 'text')


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = ('title', 'kind', 'inn', 'email', 'phone', 'address', 'orders')


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('title', 'sector', 'serial', 'code', 'cost',)


class SectorSerializer(serializers.ModelSerializer):
    equipments = EquipmentSerializer(many=True)

    class Meta:
        model = Sector
        fields = ('title', 'order', 'manager', 'equipments')


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('title', 'order', 'unit', 'quantity', 'cost', 'total')
