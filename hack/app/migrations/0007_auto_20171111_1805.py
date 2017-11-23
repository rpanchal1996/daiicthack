# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-11 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_borrowtractor_lendtractor'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowtractor',
            name='fullfilled',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='borrowtractor',
            name='quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lendtractor',
            name='fullfilled',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lendtractor',
            name='quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]