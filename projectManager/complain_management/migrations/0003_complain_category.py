# Generated by Django 3.2 on 2021-07-03 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complain_management', '0002_auto_20210703_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='complain_management.complaincategory'),
        ),
    ]