# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_skillcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillcategory',
            options={'verbose_name_plural': 'skill categories'},
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(default=1, to='resume.SkillCategory'),
            preserve_default=False,
        ),
    ]
