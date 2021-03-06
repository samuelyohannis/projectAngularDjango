# Generated by Django 3.2 on 2021-07-31 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='city_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contenent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='contenent_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='country_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('Contenent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='location_management.contenent')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='region_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.country')),
            ],
        ),
        migrations.CreateModel(
            name='SubCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='city_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.city')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='zone_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.region')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaKebele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='kebele_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('sub_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.subcity')),
            ],
        ),
        migrations.CreateModel(
            name='Wereda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='wereda_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_management.zone')),
            ],
        ),
        migrations.CreateModel(
            name='Kebele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='kebele_images')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.city')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='wereda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.wereda'),
        ),
    ]
