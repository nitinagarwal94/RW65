# Generated by Django 3.1.1 on 2021-04-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0005_warehouse_minimum_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='price_per_item',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
