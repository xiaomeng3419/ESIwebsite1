# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connor', '0004_auto_20170508_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='locationconf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, null=True)),
                ('page', models.CharField(max_length=5, null=True)),
                ('li', models.CharField(max_length=5, null=True)),
                ('time', models.DateField(null=True)),
            ],
        ),
    ]
