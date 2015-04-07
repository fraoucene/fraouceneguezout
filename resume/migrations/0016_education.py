# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=255, verbose_name=b'School')),
                ('start_on', models.DateField(verbose_name=b'Start on')),
                ('end_on', models.DateField(null=True, verbose_name=b'End on', blank=True)),
                ('current', models.BooleanField(default=False, verbose_name=b'Current')),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
