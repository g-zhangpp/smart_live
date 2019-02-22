# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('beauty', models.CharField(max_length=20)),
                ('faceshape', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='face',
            name='age',
        ),
        migrations.RemoveField(
            model_name='face',
            name='beauty',
        ),
        migrations.RemoveField(
            model_name='face',
            name='faceshape',
        ),
        migrations.RemoveField(
            model_name='face',
            name='gender',
        ),
        migrations.AddField(
            model_name='image',
            name='faceid',
            field=models.ForeignKey(to='camera.Face'),
        ),
    ]
