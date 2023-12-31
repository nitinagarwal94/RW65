# Generated by Django 3.1.1 on 2021-06-09 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0019_signature'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMTPCred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=1000, unique=True)),
                ('port', models.IntegerField()),
                ('username', models.CharField(max_length=1000, unique=True)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='settings',
            name='smtp_support',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settings',
            name='smtp_creds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='yard.smtpcred'),
        ),
    ]
