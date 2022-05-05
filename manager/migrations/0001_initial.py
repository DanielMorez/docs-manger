# Generated by Django 3.2.13 on 2022-05-05 08:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('kind', models.PositiveSmallIntegerField(choices=[(0, 'ИП'), (1, 'ООО'), (2, 'Физ. лицо')], verbose_name='Тип')),
                ('inn', models.PositiveSmallIntegerField(verbose_name='ИНН')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. почта')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='Дата начала')),
                ('ended', models.DateTimeField(verbose_name='Дата окончания работ')),
                ('is_active', models.BooleanField(default=True, verbose_name='В работе?')),
                ('priority', models.PositiveSmallIntegerField(choices=[(0, 'Низкий'), (1, 'Средний'), (2, 'Высокий')], verbose_name='Приоритет')),
                ('text', models.TextField(verbose_name='Описание работ')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='manager.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('order', models.PositiveSmallIntegerField(unique=True, verbose_name='Номер')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sectors', to=settings.AUTH_USER_MODEL, verbose_name='Ответственный')),
            ],
            options={
                'verbose_name': 'Участок',
                'verbose_name_plural': 'Участки',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='TechnicalProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Порядковый номер')),
                ('text', models.TextField(verbose_name='Описание')),
                ('form', models.PositiveSmallIntegerField(choices=[(0, 'Единичные'), (1, 'Типовые'), (2, 'Групповые')], verbose_name='Форма организации')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='manager.order', verbose_name='Участок работ')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='manager.sector', verbose_name='Участок работ')),
            ],
            options={
                'verbose_name': 'Технический процесс',
                'verbose_name_plural': 'Технический процесс',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('unit', models.PositiveSmallIntegerField(choices=[(0, 'м³'), (1, 'дм³'), (2, 'Кг'), (3, 'Гр'), (4, 'Т')], verbose_name='Единица измерения')),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=7, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Количество')),
                ('cost', models.DecimalField(decimal_places=1, max_digits=7, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Стоимость за единицу')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='manager.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Ресурс',
                'verbose_name_plural': 'Ресурсы',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('serial', models.CharField(max_length=255, verbose_name='Серия (номер)')),
                ('code', models.CharField(max_length=255, verbose_name='Код')),
                ('cost', models.DecimalField(decimal_places=1, max_digits=7, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Стоимость')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='manager.sector', verbose_name='Участок')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудование',
            },
        ),
    ]
