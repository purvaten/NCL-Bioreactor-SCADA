# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scada', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='values',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='values',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
    ]
