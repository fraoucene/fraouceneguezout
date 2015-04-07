# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_remove_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='row',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Row (1 or 2)', choices=[(1, b'Primary skills'), (2, b'Secondary skills')]),
            preserve_default=True,
        ),
    ]
