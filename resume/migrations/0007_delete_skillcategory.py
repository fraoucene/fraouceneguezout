# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_remove_skill_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SkillCategory',
        ),
    ]
