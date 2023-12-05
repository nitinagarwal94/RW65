# Generated by Django 3.1.1 on 2021-04-22 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0002_auto_20210412_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='balance_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='article',
            name='entry_weight',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='article',
            name='outgoing_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='article',
            name='price1',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price2',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price3',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price4',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price5',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='buildingsite',
            name='infotext',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='container',
            name='maximum_gross_weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='tare_weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='price_group',
            field=models.CharField(blank=True, choices=[('price1', 'Price 1'), ('price2', 'Price 2'), ('price3', 'Price 3'), ('price4', 'Price 4'), ('price5', 'Price 5')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='article',
            field=models.CharField(choices=[('Material', 'Material'), ('Produkt', 'Produkt'), ('Artikel', 'Artikel'), ('Article', 'Article')], max_length=40, null=True),
        ),
    ]