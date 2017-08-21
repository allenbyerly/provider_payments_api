# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('social_security_number', models.CharField(max_length=255)),
                ('date_of_birth', models.DateTimeField()),
                ('gender', models.CharField(max_length=255)),
                ('ethnicity', models.CharField(max_length=255)),
                ('preferred_language', models.CharField(max_length=255)),
                ('race', models.CharField(max_length=255)),
                ('doctor', models.IntegerField()),
                ('primary_care_physician', models.CharField(max_length=255)),
                ('chart_id', models.CharField(max_length=255)),
                ('patient_payment_profile', models.CharField(max_length=255)),
                ('default_pharmacy', models.CharField(max_length=255)),
                ('responsible_party_name', models.CharField(max_length=255)),
                ('responsible_party_relation', models.CharField(max_length=255)),
                ('responsible_party_phone', models.CharField(max_length=255)),
                ('responsible_party_email', models.CharField(max_length=255)),
                ('offices', models.CharField(max_length=255)),
                ('since', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('home_phone', models.CharField(max_length=255)),
                ('cell_phone', models.CharField(max_length=255)),
                ('employer_address', models.CharField(max_length=255)),
                ('employer_city', models.CharField(max_length=255)),
                ('employer_state', models.CharField(max_length=255)),
                ('employer_zip_code', models.CharField(max_length=255)),
                ('emergency_contact_name', models.CharField(max_length=255)),
                ('emergency_contact_phone', models.CharField(max_length=255)),
                ('emergency_contact_relation', models.CharField(max_length=255)),
                ('employer', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Provider',
        ),
    ]