# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_auto_20150221_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigurationTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(default=b'Default', unique=True, max_length=255, verbose_name=b'Label')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('subtitle', models.CharField(max_length=255, verbose_name=b'Subtitle')),
                ('about', models.CharField(max_length=255, null=True, verbose_name=b'About secton', blank=True)),
                ('skills', models.CharField(max_length=255, verbose_name=b'Skills section')),
                ('experiences', models.CharField(max_length=255, verbose_name=b'Experiences section')),
                ('education', models.CharField(max_length=255, verbose_name=b'Education section')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
