# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_delete_skillcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='label',
            field=models.CharField(default='Label', max_length=255, verbose_name=b'Skill'),
            preserve_default=False,
        ),
    ]
