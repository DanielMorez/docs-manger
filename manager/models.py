from manager.constants import UNITS, CUSTOMER_TYPES, PRIORITY, FORMS
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Customer(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    kind = models.PositiveSmallIntegerField(
        verbose_name='Тип',
        choices=CUSTOMER_TYPES
    )
    inn = models.PositiveSmallIntegerField(
        verbose_name='ИНН'
    )
    email = models.EmailField(
        verbose_name='Эл. почта'
    )
    address = models.TextField(
        verbose_name='Адрес'
    )
    phone = PhoneNumberField(
        verbose_name='Номер телефона'
    )

    class Meta:
        verbose_name = _('Организация')
        verbose_name_plural = _('Организации')

    def __str__(self):
        return f'{self.title}'


class Sector(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    order = models.PositiveSmallIntegerField(
        verbose_name='Номер',
        unique=True
    )
    manager = models.ForeignKey(
        to=User,
        verbose_name='Ответственный',
        related_name='sectors',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('order',)
        verbose_name = _('Участок')
        verbose_name_plural = _('Участки')

    def __str__(self):
        return f'#{self.order} {self.title}'


class Resource(models.Model):
    order = models.ForeignKey(
        to='Order',
        verbose_name='Заказ',
        related_name='resources',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    unit = models.PositiveSmallIntegerField(
        verbose_name='Единица измерения',
        choices=UNITS
    )
    quantity = models.DecimalField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(0.1),
        ],
        decimal_places=1,
        max_digits=7,
    )
    cost = models.DecimalField(
        verbose_name='Стоимость за единицу',
        validators=[
            MinValueValidator(0.1),
        ],
        decimal_places=1,
        max_digits=7,
    )

    class Meta:
        verbose_name = _('Ресурс')
        verbose_name_plural = _('Ресурсы')

    def __str__(self):
        return f'{self.title} (Итоговая стоймость: {self.total})'

    @property
    def total(self):
        return self.quantity * self.cost

    total.fget.short_description = 'Итог'


class Equipment(models.Model):
    sector = models.ForeignKey(
        to=Sector,
        verbose_name='Участок',
        related_name='equipments',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    serial = models.CharField(
        verbose_name='Серия (номер)',
        max_length=255
    )
    code = models.CharField(
        verbose_name='Код',
        max_length=255
    )
    cost = models.DecimalField(
        verbose_name='Стоимость',
        validators=[
            MinValueValidator(0.1),
        ],
        decimal_places=1,
        max_digits=7,
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=1
    )

    @property
    def total(self):
        return self.quantity * self.cost

    total.fget.short_description = 'Итог'

    class Meta:
        verbose_name = _('Оборудование')
        verbose_name_plural = _('Оборудование')

    def __str__(self):
        return f'{self.title} #{self.serial} (общая сумма {self.total})'


class Order(models.Model):
    created = models.DateTimeField(
        verbose_name='Дата начала'
    )
    ended = models.DateTimeField(
        verbose_name='Дата окончания работ'
    )
    customer = models.ForeignKey(
        to=Customer,
        verbose_name='Клиент',
        related_name='orders',
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        verbose_name='В работе?',
        default=True
    )
    priority = models.PositiveSmallIntegerField(
        verbose_name='Приоритет',
        choices=PRIORITY
    )
    text = models.TextField(
        verbose_name='Описание работ'
    )

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return f'{self.customer}: с {self.created} по {self.ended}'


class TechnicalProcess(models.Model):
    booking = models.ForeignKey(
        to=Order,
        verbose_name='Заказ',
        related_name='processes',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name='Наименование',
        max_length=255
    )
    order = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер',
    )
    sector = models.ForeignKey(
        to=Sector,
        verbose_name='Участок работ',
        related_name='orders',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Описание'
    )
    form = models.PositiveSmallIntegerField(
        verbose_name='Форма организации',
        choices=FORMS
    )

    class Meta:
        ordering = ('order',)
        verbose_name = _('Технический процесс')
        verbose_name_plural = _('Технический процесс')

    def __str__(self):
        return f'{self.title}'
