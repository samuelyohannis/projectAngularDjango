# Generated by Django 3.2 on 2021-05-22 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment_management', '0006_auto_20210521_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kebeleprojectcomment',
            old_name='user',
            new_name='profile',
        ),
    ]
