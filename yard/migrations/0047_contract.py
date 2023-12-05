# Generated by Django 3.1.1 on 2021-07-07 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0046_container_ss_role_access'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_number', models.CharField(max_length=1000, primary_key=True, serialize=False, unique=True)),
                ('agreed_value', models.BigIntegerField()),
                ('signature', models.FileField(upload_to='contract_signatures/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yard.article')),
                ('construction_site', models.ManyToManyField(to='yard.BuildingSite')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yard.customer')),
                ('vehicles', models.ManyToManyField(to='yard.Vehicle')),
            ],
        ),
    ]