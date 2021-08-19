# Generated by Django 3.2 on 2021-08-10 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0003_alter_countryprojectfile_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityprojectfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.cityproject'),
        ),
        migrations.AlterField(
            model_name='cityprojectreport',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.cityproject'),
        ),
        migrations.AlterField(
            model_name='kebeleprojectfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.kebeleproject'),
        ),
        migrations.AlterField(
            model_name='kebeleprojectreport',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.kebeleproject'),
        ),
        migrations.AlterField(
            model_name='regionprojectfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.regionproject'),
        ),
        migrations.AlterField(
            model_name='regionprojectreport',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.regionproject'),
        ),
        migrations.AlterField(
            model_name='subcityprojectfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.subcityproject'),
        ),
        migrations.AlterField(
            model_name='subcityprojectreport',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.subcityproject'),
        ),
        migrations.AlterField(
            model_name='weredakebeleprojectfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.weredakebeleproject'),
        ),
        migrations.AlterField(
            model_name='weredakebeleprojectreport',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.weredakebeleproject'),
        ),
        migrations.AlterField(
            model_name='weredaprojectfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.weredaproject'),
        ),
        migrations.AlterField(
            model_name='weredaprojectreport',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.weredaproject'),
        ),
        migrations.AlterField(
            model_name='zoneprojectfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.zoneproject'),
        ),
        migrations.AlterField(
            model_name='zoneprojectreport',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.zoneproject'),
        ),
    ]