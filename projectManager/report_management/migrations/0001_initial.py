# Generated by Django 3.2 on 2021-07-31 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('desc', models.TextField()),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='file_management.file')),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report_management.report')),
            ],
        ),
    ]