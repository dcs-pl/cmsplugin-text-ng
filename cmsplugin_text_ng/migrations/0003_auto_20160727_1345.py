# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_text_ng', '0002_auto_20160421_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textngvariabletextinput',
            options={'verbose_name': 'text input', 'verbose_name_plural': 'text inputs'},
        ),
        migrations.AddField(
            model_name='textng',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name', blank=True),
        ),
        migrations.AlterField(
            model_name='textng',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
