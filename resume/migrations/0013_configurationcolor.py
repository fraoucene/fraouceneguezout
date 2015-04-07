# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_configurationtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigurationColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(default=b'Default', unique=True, max_length=255, verbose_name=b'Label')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('title_color', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Title')),
                ('subtitle_color', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Subtitle')),
                ('about_title', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Title')),
                ('about_body', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Body')),
                ('skills_title', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Title')),
                ('skills_label', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Label')),
                ('experiences_company', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Company')),
                ('experiences_duration', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Duration')),
                ('experiences_description', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Description')),
                ('education_school', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'School')),
                ('education_duration', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Duration')),
                ('education_description', models.CharField(default=b'#FFFFFF', max_length=7, verbose_name=b'Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
