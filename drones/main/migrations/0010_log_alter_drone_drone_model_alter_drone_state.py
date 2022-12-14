# Generated by Django 4.1 on 2022-12-01 03:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_drone_drone_model_alter_drone_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drone', models.CharField(max_length=100)),
                ('battery_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('state', models.CharField(max_length=25)),
                ('state_changed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='drone',
            name='drone_model',
            field=models.CharField(choices=[('Heavyweight', 'Heavyweight'), ('Middleweight', 'Middleweight'), ('Lightweight', 'Lightweight'), ('Cruiseweight', 'Cruiseweight')], max_length=25),
        ),
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(choices=[('DELIVERED', 'DELIVERED'), ('IDLE', 'IDLE'), ('LOADED', 'LOADED'), ('RETURNING', 'RETURNING'), ('DELIVERING', 'DELIVERING'), ('LOADING', 'LOADING')], max_length=25),
        ),
    ]
