# Generated by Django 3.2 on 2021-07-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0008_auto_20210723_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryproject',
            name='img',
            field=models.ImageField(default='images/project-logo.png', null=True, upload_to='images/countryProject'),
        ),
    ]