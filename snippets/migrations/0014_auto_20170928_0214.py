# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0013_auto_20170926_1133'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='camerainfo',
            name='isOnLine',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
