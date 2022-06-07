from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from manager.models import Resource, Customer, Order


class ManagerTestCase(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(
            title='Фабрика',
            kind=0,
            inn='123123',
            email='ivanov@mail.com',
            address='Адрес',
            phone='+79991231231'
        )
        self.order = Order.objects.create(
            created=timezone.now(),
            ended=timezone.now(),
            customer=self.customer,
            priority=0,
            text='Текст'
        )
        self.resource = Resource.objects.create(
            order=self.order,
            title='Картон',
            unit=0,
            quantity=10,
            cost=10
        )

    def test_total_resource(self):
        """ Correct work when calculating the total """
        self.assertTrue(self.resource.total == 100, 'Resource total correctly works')
        print('Resource total correctly works')

    def test_validate_phone(self):
        self.customer.phone = 'qwerty'
        self.customer.save()
        try:
            self.customer.full_clean()
        except ValidationError as e:
            print('Correctly validate phone')