# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeatOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MeatPrice',
            fields=[
                ('name', models.CharField(default='', max_length=254, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eating_date', models.DateTimeField()),
                ('deposit_status', models.CharField(choices=[('W', 'Waiting'), ('C', 'Complete')], default='W', max_length=1)),
                ('is_delivery', models.BooleanField(default=True)),
                ('delivery_location', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Orderer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('password', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='orderer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Orderer'),
        ),
        migrations.AddField(
            model_name='meatorder',
            name='meat_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.MeatPrice'),
        ),
        migrations.AddField(
            model_name='meatorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
    ]
