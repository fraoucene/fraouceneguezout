# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_auto_20150221_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationtitle',
            name='about',
            field=models.CharField(max_length=255, null=True, verbose_name=b'About section', blank=True),
            preserve_default=True,
        ),
    ]
