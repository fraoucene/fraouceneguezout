# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20150203_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillcategory',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
    ]
