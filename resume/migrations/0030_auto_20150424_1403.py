# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0029_auto_20150424_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='detail_fr',
            field=models.TextField(null=True, verbose_name=b'Detail FR', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='title_fr',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Title FR', blank=True),
            preserve_default=True,
        ),
    ]
