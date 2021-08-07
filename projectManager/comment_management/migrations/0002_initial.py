# Generated by Django 3.2 on 2021-08-03 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0002_profile_country'),
        ('project_management', '0001_initial'),
        ('level_management', '0001_initial'),
        ('comment_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoneprojectcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.zoneproject'),
        ),
        migrations.AddField(
            model_name='weredaprojectcomment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='weredaprojectcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.weredaproject'),
        ),
        migrations.AddField(
            model_name='weredakebeleprojectcomment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='weredakebeleprojectcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.weredakebeleproject'),
        ),
        migrations.AddField(
            model_name='subcityprojectcomment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='subcityprojectcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.subcityproject'),
        ),
        migrations.AddField(
            model_name='regionprojectcomment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='regionprojectcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.regionproject'),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='level',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='level_management.level'),
        ),
        migrations.AddField(
            model_name='kebeleprojectcomment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='kebeleprojectcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.kebeleproject'),
        ),
        migrations.AddField(
            model_name='countryprojectcomment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='countryprojectcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.countryproject'),
        ),
        migrations.AddField(
            model_name='cityprojectcomment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='cityprojectcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.cityproject'),
        ),
    ]