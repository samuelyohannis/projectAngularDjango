# Generated by Django 3.2 on 2021-08-20 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='isViewed',
            new_name='is_viewed',
        ),
    ]