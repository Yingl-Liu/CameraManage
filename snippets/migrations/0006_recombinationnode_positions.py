# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_remove_recombinationnode_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='recombinationnode',
            name='positions',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]