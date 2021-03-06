# Generated by Django 3.2 on 2021-08-30 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0013_alter_countryprojectstackeholder_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryProjectReportReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('mark_percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.countryprojectreport')),
            ],
        ),
        migrations.DeleteModel(
            name='CountryProjectReportAssessment',
        ),
    ]
