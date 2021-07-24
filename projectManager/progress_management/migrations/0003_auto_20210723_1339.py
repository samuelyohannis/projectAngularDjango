# Generated by Django 3.2 on 2021-07-23 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_management', '0001_initial'),
        ('progress_management', '0002_progress_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progressfile',
            name='date',
        ),
        migrations.RemoveField(
            model_name='progressfile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='progressfile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='progressfile',
            name='url',
        ),
        migrations.RemoveField(
            model_name='progressfile',
            name='views',
        ),
        migrations.AddField(
            model_name='progressfile',
            name='file_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='file_management.file'),
            preserve_default=False,
        ),
    ]