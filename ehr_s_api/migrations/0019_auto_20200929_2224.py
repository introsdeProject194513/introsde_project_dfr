# Generated by Django 3.0.10 on 2020-09-29 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehr_s_api', '0018_auto_20200929_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='drug_interaction',
            new_name='drug_interactions',
        ),
    ]