# Generated by Django 3.0.5 on 2020-06-14 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_auto_20200521_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
    ]
