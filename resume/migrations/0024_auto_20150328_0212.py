# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0023_auto_20150327_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='detail',
            field=models.TextField(null=True, verbose_name=b'Detail', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='lien',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Lien', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.TextField(null=True, verbose_name=b'Location', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Title', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='tools',
            field=models.TextField(null=True, verbose_name=b'Tools', blank=True),
            preserve_default=True,
        ),
    ]
