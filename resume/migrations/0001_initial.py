# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Skill')),
                ('grade', models.PositiveIntegerField(default=100, verbose_name=b'Grade (%)')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
