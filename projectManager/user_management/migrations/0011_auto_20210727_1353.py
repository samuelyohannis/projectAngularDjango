# Generated by Django 3.2 on 2021-07-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0010_auto_20210727_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='worklevel',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]