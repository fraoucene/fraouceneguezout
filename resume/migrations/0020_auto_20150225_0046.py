# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0019_auto_20150225_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configurationcolor',
            name='about_title',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='education_title',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='experiences_title',
        ),
        migrations.RemoveField(
            model_name='configurationcolor',
            name='skills_title',
        ),
        migrations.AddField(
            model_name='configurationcolor',
            name='about',
            field=models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'About title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configurationcolor',
            name='education',
            field=models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Education title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configurationcolor',
            name='experiences',
            field=models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Experiences title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configurationcolor',
            name='skills',
            field=models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Skills title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configurationtitle',
            name='about',
            field=models.CharField(max_length=255, null=True, verbose_name=b'About title', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configurationtitle',
            name='education',
            field=models.CharField(max_length=255, verbose_name=b'Education title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configurationtitle',
            name='experiences',
            field=models.CharField(max_length=255, verbose_name=b'Experiences title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configurationtitle',
            name='skills',
            field=models.CharField(max_length=255, verbose_name=b'Skills title'),
            preserve_default=True,
        ),
    ]
