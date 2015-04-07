# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0022_auto_20150325_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='detail',
            field=models.TextField(null=True, verbose_name=b'Detail', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='lien',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Lien', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.TextField(null=True, verbose_name=b'Location', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Title', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='tools',
            field=models.TextField(null=True, verbose_name=b'Tools', blank=True),
            preserve_default=True,
        ),
    ]
