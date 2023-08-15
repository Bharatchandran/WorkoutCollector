# Generated by Django 4.2.4 on 2023-08-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheduling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Workout Date')),
                ('workout_time', models.CharField(choices=[('M', 'Morning'), ('E', 'Evening'), ('N', 'Night')], default='M', max_length=2)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.workout')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
