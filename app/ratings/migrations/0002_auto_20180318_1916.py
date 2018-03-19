# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='route_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('route_id', 'user_id')]),
        ),
    ]