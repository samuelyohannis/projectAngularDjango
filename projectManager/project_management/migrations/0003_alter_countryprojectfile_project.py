# Generated by Django 3.2 on 2021-08-09 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0002_auto_20210808_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryprojectfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.countryproject'),
        ),
    ]
