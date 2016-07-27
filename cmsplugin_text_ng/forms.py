# -*- coding: utf-8 -*-
from django import forms

from .models import TextNG


class PluginAddForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'template',)
        model = TextNG


class PluginEditForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'body',)
        model = TextNG
