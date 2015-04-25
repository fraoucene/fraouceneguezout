# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0031_experience_description_fr'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='description_fr',
            field=models.TextField(null=True, verbose_name=b'Description FR', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='detail_fr',
            field=models.TextField(null=True, verbose_name=b'Detail FR', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='title_fr',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Title FR', blank=True),
            preserve_default=True,
        ),
    ]
