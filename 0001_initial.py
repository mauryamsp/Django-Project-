# Generated by Django 5.0.7 on 2024-08-04 08:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=100)),
                ('Question', models.TextField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
