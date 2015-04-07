# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20150206_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='category',
        ),
    ]
