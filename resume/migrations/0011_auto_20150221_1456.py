# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_skill_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='grade',
            field=models.PositiveIntegerField(default=100, verbose_name=b'Grade'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skill',
            name='row',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Row', choices=[(1, b'Primary skills'), (2, b'Secondary skills')]),
            preserve_default=True,
        ),
    ]
