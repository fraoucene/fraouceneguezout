# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_skill_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='name',
        ),
    ]
