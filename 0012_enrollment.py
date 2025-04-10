# Generated by Django 5.0.7 on 2024-08-11 17:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0011_delete_enrollment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=45, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=100)),
                ('choose_course', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('fee_status', models.BooleanField(default=False)),
                ('duration', models.IntegerField(default=0)),
                ('resource_file', models.FileField(blank=True, null=True, upload_to='class_app/resourses')),
                ('stu_pic', models.ImageField(blank=True, null=True, upload_to='class_app/student_picture')),
            ],
        ),
    ]
