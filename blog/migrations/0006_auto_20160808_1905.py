# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160803_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ages',
            field=models.CharField(choices=[('16+', '16+'), ('18+', '18+'), ('19+', '19+'), ('21+', '21+'), ('All Ages', 'All Ages')], default='All Ages', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='songs',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
