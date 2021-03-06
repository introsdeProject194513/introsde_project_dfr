# Generated by Django 3.1.1 on 2020-09-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('icd_code', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('substance_name', models.CharField(max_length=60)),
                ('product_type', models.CharField(max_length=60)),
                ('brand_name', models.CharField(max_length=60)),
                ('dosage_form', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('tax_code', models.CharField(max_length=16)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_date', models.DateTimeField()),
                ('prescription_validity', models.DateTimeField()),
                ('note', models.CharField(max_length=200)),
                ('drug', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ehr_s_api.drug')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ehr_s_api.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ehr_s_api.disease')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ehr_s_api.patient')),
            ],
        ),
    ]
