# Generated by Django 5.0.7 on 2024-08-06 16:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0005_studyresources'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_content', models.TextField(max_length=100)),
                ('notice_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
