# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taletelling', '0004_auto_20181121_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='file',
            field=models.FileField(upload_to='story/'),
        ),
    ]
