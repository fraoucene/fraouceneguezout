# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0026_remove_experience_title_fr'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('label_fr', models.CharField(max_length=255, verbose_name=b'Label FR')),
                ('label_en', models.CharField(max_length=255, verbose_name=b'Label EN')),
                ('subtitle_fr', models.CharField(max_length=255, verbose_name=b'Subtitle FR')),
                ('subtitle_en', models.CharField(max_length=255, verbose_name=b'Subtitle EN')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
