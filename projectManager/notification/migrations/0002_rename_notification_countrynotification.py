# Generated by Django 3.2 on 2021-08-30 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_profile_country'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='CountryNotification',
        ),
    ]
