# Generated by Django 3.0.10 on 2020-09-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehr_s_api', '0012_remove_patient_deleted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
