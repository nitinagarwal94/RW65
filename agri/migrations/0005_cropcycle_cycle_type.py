# Generated by Django 3.1.1 on 2021-06-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0004_location_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropcycle',
            name='cycle_type',
            field=models.CharField(choices=[('YR', 'YEARLY'), ('LYR', 'LESS THAN A YEAR')], default='YR', max_length=100),
        ),
    ]
