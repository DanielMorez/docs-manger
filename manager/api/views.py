from rest_framework import generics
from manager.models import Customer

from manager.api.serializers import CustomerSerializer


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
