# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0030_auto_20150424_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='description_fr',
            field=models.TextField(null=True, verbose_name=b'Description FR', blank=True),
            preserve_default=True,
        ),
    ]
