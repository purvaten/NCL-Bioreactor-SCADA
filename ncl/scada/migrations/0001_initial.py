# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'anonymous', max_length=100)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pressure', models.FloatField(default=0.0)),
                ('temperature', models.FloatField(default=0.0)),
                ('ph', models.FloatField(default=0.0)),
                ('levels', models.FloatField(default=0.0)),
            ],
        ),
    ]
