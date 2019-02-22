# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taletelling', '0002_auto_20181120_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='file',
            field=models.FileField(upload_to='static'),
        ),
    ]
