# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-06-04 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default=0, max_length=254, verbose_name='邮箱'),
            preserve_default=False,
        ),
    ]
