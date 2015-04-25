# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0028_auto_20150424_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body_fr',
            field=models.TextField(null=True, verbose_name=b'Body FR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='about',
            name='title_fr',
            field=models.CharField(max_length=255, verbose_name=b'Title FR'),
            preserve_default=True,
        ),
    ]
