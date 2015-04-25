# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0027_titleconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='body_fr',
            field=models.TextField(null=True, verbose_name=b'Body', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='about',
            name='title_fr',
            field=models.CharField(default='', max_length=255, verbose_name=b'Title'),
            preserve_default=False,
        ),
    ]
