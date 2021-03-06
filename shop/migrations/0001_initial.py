# Generated by Django 3.0 on 2019-12-26 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название магазина')),
                ('address', models.CharField(max_length=30, verbose_name='Адрес магазина')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
                ('producer', models.CharField(max_length=30, verbose_name='Прозводитель')),
                ('release_date', models.DateField(verbose_name='Дата изготовления')),
                ('price', models.DecimalField(decimal_places=2, help_text='*в рублях', max_digits=7, verbose_name='Цена')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop', verbose_name='Магазин')),
            ],
        ),
    ]
