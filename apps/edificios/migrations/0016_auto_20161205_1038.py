# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edificios', '0015_banco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banco',
            old_name='Banco',
            new_name='banco',
        ),
        migrations.RenameField(
            model_name='banco',
            old_name='Propiedad',
            new_name='propiedad',
        ),
    ]