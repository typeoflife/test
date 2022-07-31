# Generated by Django 4.0.6 on 2022-07-30 01:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('^\\d{11}$', 'Number must be 11 digits', 'Invalid number')], verbose_name='Номер телефона'),
        ),
    ]