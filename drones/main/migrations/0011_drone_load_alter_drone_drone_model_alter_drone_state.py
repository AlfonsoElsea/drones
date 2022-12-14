# Generated by Django 4.1 on 2022-12-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_log_alter_drone_drone_model_alter_drone_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='load',
            field=models.ManyToManyField(through='main.Load', to='main.medication'),
        ),
        migrations.AlterField(
            model_name='drone',
            name='drone_model',
            field=models.CharField(choices=[('Lightweight', 'Lightweight'), ('Cruiseweight', 'Cruiseweight'), ('Heavyweight', 'Heavyweight'), ('Middleweight', 'Middleweight')], max_length=25),
        ),
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(choices=[('IDLE', 'IDLE'), ('LOADING', 'LOADING'), ('LOADED', 'LOADED'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED'), ('RETURNING', 'RETURNING')], max_length=25),
        ),
    ]
