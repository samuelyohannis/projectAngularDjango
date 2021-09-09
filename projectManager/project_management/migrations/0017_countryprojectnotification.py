# Generated by Django 3.2 on 2021-09-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0016_countrynotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryProjectNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recieved_from', models.IntegerField(null=True)),
                ('send_to', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('is_viewed', models.BooleanField(default=False)),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
