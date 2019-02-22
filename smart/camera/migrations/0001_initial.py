# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.ImageField(upload_to='media')),
                ('age', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('beauty', models.CharField(max_length=20)),
                ('faceshape', models.CharField(max_length=20)),
            ],
        ),
    ]
