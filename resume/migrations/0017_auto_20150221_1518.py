# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0016_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configurationcolor',
            old_name='subtitle_color',
            new_name='subtitle',
        ),
        migrations.RenameField(
            model_name='configurationcolor',
            old_name='title_color',
            new_name='title',
        ),
    ]
