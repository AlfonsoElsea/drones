# Generated by Django 4.1 on 2022-11-30 04:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_drone_sate_drone_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='drone_model',
            field=models.CharField(choices=[('Heavyweight', 'Heavyweight'), ('Lightweight', 'Lightweight'), ('Middleweight', 'Middleweight'), ('Cruiseweight', 'Cruiseweight')], max_length=25),
        ),
        migrations.AlterField(
            model_name='drone',
            name='serial_number',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^-?\\d+\\Z', 'Serial Number must contain only numbers')]),
        ),
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(choices=[('LOADED', 'LOADED'), ('LOADING', 'LOADING'), ('DELIVERED', 'DELIVERED'), ('DELIVERING', 'DELIVERING'), ('RETURNING', 'RETURNING'), ('IDLE', 'IDLE')], max_length=25),
        ),
        migrations.AlterField(
            model_name='medication',
            name='code',
            field=models.CharField(max_length=25, validators=[django.core.validators.RegexValidator('^[A-Z0-9_]+\\Z', 'Incorrect name format')]),
        ),
        migrations.AlterField(
            model_name='medication',
            name='name',
            field=models.CharField(max_length=25, validators=[django.core.validators.RegexValidator('^[-a-zA-Z0-9_]+\\Z', 'Incorrect name format')]),
        ),
    ]