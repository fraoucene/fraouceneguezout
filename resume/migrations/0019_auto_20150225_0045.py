# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_auto_20150222_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configurationcolor',
            name='about_body',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='education_description',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='education_duration',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='education_school',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='experiences_company',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='experiences_description',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='experiences_duration',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='skills_label',
        ),
        migrations.AddField(
            model_name='configurationcolor',
            name='education_title',
            field=models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configurationcolor',
            name='experiences_title',
            field=models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Title'),
            preserve_default=True,
        ),
    ]
