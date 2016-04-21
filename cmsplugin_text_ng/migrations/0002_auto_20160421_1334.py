# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import filer.fields.file
import django.core.validators
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cmsplugin_text_ng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextNGVariableFilerFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20, verbose_name='label', validators=[django.core.validators.RegexValidator(regex=b'[_a-z]+', message='Only lower case characters.')])),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
        ),
        migrations.CreateModel(
            name='TextNGVariableFilerImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20, verbose_name='label', validators=[django.core.validators.RegexValidator(regex=b'[_a-z]+', message='Only lower case characters.')])),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='TextNGVariableHTML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20, verbose_name='label', validators=[django.core.validators.RegexValidator(regex=b'[_a-z]+', message='Only lower case characters.')])),
                ('value', djangocms_text_ckeditor.fields.HTMLField(null=True, verbose_name='value')),
            ],
            options={
                'verbose_name': 'html text',
                'verbose_name_plural': 'html texts',
            },
        ),
        migrations.CreateModel(
            name='TextNGVariableTextInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20, verbose_name='label', validators=[django.core.validators.RegexValidator(regex=b'[_a-z]+', message='Only lower case characters.')])),
                ('value', models.CharField(max_length=1000, null=True, verbose_name='value')),
            ],
            options={
                'verbose_name': 'text input',
                'verbose_name_plural': 'text input',
            },
        ),
        migrations.AlterField(
            model_name='textng',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_text_ng_textng', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='textngvariabletext',
            name='text_ng',
            field=models.ForeignKey(to='cmsplugin_text_ng.TextNG'),
        ),
        migrations.AddField(
            model_name='textngvariabletextinput',
            name='text_ng',
            field=models.ForeignKey(to='cmsplugin_text_ng.TextNG'),
        ),
        migrations.AddField(
            model_name='textngvariablehtml',
            name='text_ng',
            field=models.ForeignKey(to='cmsplugin_text_ng.TextNG'),
        ),
        migrations.AddField(
            model_name='textngvariablefilerimage',
            name='text_ng',
            field=models.ForeignKey(to='cmsplugin_text_ng.TextNG'),
        ),
        migrations.AddField(
            model_name='textngvariablefilerimage',
            name='value',
            field=filer.fields.image.FilerImageField(verbose_name='value', blank=True, to='filer.Image', null=True),
        ),
        migrations.AddField(
            model_name='textngvariablefilerfile',
            name='text_ng',
            field=models.ForeignKey(to='cmsplugin_text_ng.TextNG'),
        ),
        migrations.AddField(
            model_name='textngvariablefilerfile',
            name='value',
            field=filer.fields.file.FilerFileField(verbose_name='value', blank=True, to='filer.File', null=True),
        ),
    ]
