# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20150203_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(related_name='skills', to='resume.SkillCategory'),
            preserve_default=True,
        ),
    ]
