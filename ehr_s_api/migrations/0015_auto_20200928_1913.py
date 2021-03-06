# Generated by Django 3.0.10 on 2020-09-28 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ehr_s_api', '0014_measurement_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
