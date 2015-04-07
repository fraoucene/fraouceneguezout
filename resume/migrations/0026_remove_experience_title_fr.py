# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0025_experience_title_fr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='title_fr',
        ),
    ]
