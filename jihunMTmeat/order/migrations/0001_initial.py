# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 14:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orderer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone length has to be 11 & Only number', regex='^\\d{11}$')])),
                ('password', models.CharField(default='', max_length=254)),
                ('eating_date', models.DateTimeField()),
                ('deposit_status', models.CharField(choices=[('W', 'Waiting'), ('C', 'Complete')], max_length=1)),
                ('is_delivery', models.BooleanField(default=False)),
            ],
        ),
    ]
