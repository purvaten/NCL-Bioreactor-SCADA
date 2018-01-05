# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
