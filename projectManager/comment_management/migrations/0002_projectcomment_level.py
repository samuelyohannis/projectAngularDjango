# Generated by Django 3.2 on 2021-05-16 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('level_management', '0001_initial'),
        ('comment_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcomment',
            name='level',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='level_management.level'),
        ),
    ]