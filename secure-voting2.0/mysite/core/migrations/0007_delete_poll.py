# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-17 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180217_0633'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Poll',
        ),
    ]