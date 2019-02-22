# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0003_auto_20181121_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ImageField(upload_to='mesdia'),
        ),
    ]
