# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=35)),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=500)),
                ('categoria', models.CharField(max_length=35)),
            ],
        ),
    ]