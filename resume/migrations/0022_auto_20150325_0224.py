# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0021_skill_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='row',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Row', choices=[(1, b'Skills'), (2, b'Tools'), (3, b'Langages')]),
            preserve_default=True,
        ),
    ]
