# Generated by Django 3.1.1 on 2021-06-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0024_auto_20210614_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrier', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
