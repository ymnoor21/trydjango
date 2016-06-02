# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
