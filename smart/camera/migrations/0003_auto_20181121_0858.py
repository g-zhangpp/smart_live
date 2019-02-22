# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_auto_20181120_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='faceid',
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.DeleteModel(
            name='Face',
        ),
    ]
