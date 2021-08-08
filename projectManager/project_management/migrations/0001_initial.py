# Generated by Django 3.2 on 2021-08-07 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location_management', '0001_initial'),
        ('user_management', '0002_profile_country'),
        ('progress_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('catagory', models.IntegerField(null=True)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(default='images/project-logo.png', null=True, upload_to='images/cityProject')),
                ('reported', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.city')),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
            ],
        ),
        migrations.CreateModel(
            name='CountryProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('catagory', models.IntegerField(null=True)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(default='images/project-logo.png', null=True, upload_to='images/countryProject')),
                ('reported', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='location_management.country')),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
            ],
        ),
        migrations.CreateModel(
            name='KebeleProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('catagory', models.IntegerField(null=True)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(default='images/project-logo.png', null=True, upload_to='images/kebeleProject')),
                ('reported', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('kebele', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.kebele')),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegionProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('catagory', models.IntegerField(null=True)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(default='images/regionProject/regions.jpg', null=True, upload_to='images/regionProject')),
                ('reported', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.region')),
            ],
        ),
        migrations.CreateModel(
            name='SubCityProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('catagory', models.IntegerField(null=True)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(default='images/project-logo.png', null=True, upload_to='images/subCityProject')),
                ('reported', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('sub_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.subcity')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaKebeleProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('catagory', models.IntegerField(null=True)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(default='images/project-logo.png', null=True, upload_to='images/weredaKebeleProject')),
                ('reported', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('wereda_kebele', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.weredakebele')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('catagory', models.IntegerField(null=True)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(default='images/project-logo.png', null=True, upload_to='images/weredaProject')),
                ('reported', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('wereda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.wereda')),
            ],
        ),
        migrations.CreateModel(
            name='ZoneProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('catagory', models.IntegerField(null=True)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(null=True)),
                ('img', models.ImageField(default='images/project-logo.png', null=True, upload_to='images/weredaProject')),
                ('reported', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('zone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_management.zone')),
            ],
        ),
        migrations.CreateModel(
            name='ZoneProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project_management.zoneproject')),
            ],
        ),
        migrations.CreateModel(
            name='ZoneProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='progress_management.progress')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.zoneproject')),
            ],
        ),
        migrations.CreateModel(
            name='ZoneProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/zoneProJect')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.zoneproject')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project_management.weredaproject')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='progress_management.progress')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.weredaproject')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/weredaProJect')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.weredaproject')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaKebeleProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project_management.weredakebeleproject')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaKebeleProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='progress_management.progress')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.weredakebeleproject')),
            ],
        ),
        migrations.CreateModel(
            name='WeredaKebeleProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/weredaKebeleProJect')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.weredakebeleproject')),
            ],
        ),
        migrations.CreateModel(
            name='SubCityProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project_management.subcityproject')),
            ],
        ),
        migrations.CreateModel(
            name='SubCityProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='progress_management.progress')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.subcityproject')),
            ],
        ),
        migrations.CreateModel(
            name='SubCityProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/subCityProJect')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.subcityproject')),
            ],
        ),
        migrations.CreateModel(
            name='RegionProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project_management.regionproject')),
            ],
        ),
        migrations.CreateModel(
            name='RegionProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='progress_management.progress')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.regionproject')),
            ],
        ),
        migrations.CreateModel(
            name='RegionProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/regionProJect')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.regionproject')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('completion', models.IntegerField(default=0)),
                ('bujdet', models.IntegerField(default=0)),
                ('level', models.IntegerField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('desc', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('catagory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_management.projectcategory')),
            ],
        ),
        migrations.CreateModel(
            name='KebeleProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project_management.kebeleproject')),
            ],
        ),
        migrations.CreateModel(
            name='KebeleProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='progress_management.progress')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.kebeleproject')),
            ],
        ),
        migrations.CreateModel(
            name='KebeleProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/kebeleProJect')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.kebeleproject')),
            ],
        ),
        migrations.CreateModel(
            name='CountryProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.countryproject')),
            ],
        ),
        migrations.CreateModel(
            name='CountryProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='progress_management.progress')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.countryproject')),
            ],
        ),
        migrations.CreateModel(
            name='CountryProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/countryProJect')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.countryproject')),
            ],
        ),
        migrations.CreateModel(
            name='CityProjectReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worklevel', models.IntegerField(default=9)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('desc', models.TextField(default='report')),
                ('percentage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project_management.cityproject')),
            ],
        ),
        migrations.CreateModel(
            name='CityProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('progress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='progress_management.progress')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_management.cityproject')),
            ],
        ),
        migrations.CreateModel(
            name='CityProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/cityProJect')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.cityproject')),
            ],
        ),
    ]
