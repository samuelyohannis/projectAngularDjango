# Generated by Django 3.2 on 2021-07-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0006_alter_project_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionproject',
            name='img',
            field=models.ImageField(default='images/regionProject/regions.jpg', null=True, upload_to='images/regionProject'),
        ),
    ]