# -*- coding: utf-8 -*-
from django import forms

from .models import TextNG


class PluginAddForm(forms.ModelForm):

    class Meta:
        fields = ('template',)
        model = TextNG


class PluginEditForm(forms.ModelForm):

    class Meta:
        fields = ('body',)
        model = TextNG
