from django.urls import path
from .views import CustomerListAPIView


urlpatterns = [
    path('customers', CustomerListAPIView.as_view(), name='customers'),
]
