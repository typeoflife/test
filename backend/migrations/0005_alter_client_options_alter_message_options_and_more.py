# Generated by Django 4.0.6 on 2022-07-31 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Newsletter', 'verbose_name_plural': 'Newsletters'},
        ),
    ]