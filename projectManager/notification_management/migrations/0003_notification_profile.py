# Generated by Django 3.2 on 2021-08-30 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_profile_country'),
        ('notification_management', '0002_rename_isviewed_notification_is_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.profile'),
        ),
    ]
