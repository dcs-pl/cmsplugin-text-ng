import django
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .type_registry import register_type, get_type_list
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_text_ckeditor.models import AbstractText
from filer.fields.image import FilerImageField, FilerFileField


class TextNGTemplateCategory(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('template category')
        verbose_name_plural = _('template categories')
        ordering = ['title']


class TextNGTemplate(models.Model):
    category = models.ForeignKey(TextNGTemplateCategory, blank=True, null=True)
    title = models.CharField(max_length=128)
    path = models.CharField(max_length=128)

    def __unicode__(self):
        if self.category:
            return u"%s (%s)" % (self.title, self.category)
        return self.title

    class Meta:
        verbose_name = _('template')
        verbose_name_plural = _('templates')
        ordering = ['title']


@python_2_unicode_compatible
class TextNG(AbstractText):
    search_fulltext = True

    template = models.ForeignKey(TextNGTemplate)
    name = models.CharField(
        verbose_name=_("name"),
        max_length=128,
        blank=True,
    )

    def copy_relations(self, old_instance):
        for model in get_type_list():
            for instance in model.objects.filter(text_ng=old_instance):
                instance.pk = None
                instance.text_ng = self
                instance.save()

    def __str__(self):
        return self.name or force_text(self.pk)

    class Meta:
        verbose_name = _('text')
        verbose_name_plural = _('texts')


class TextNGVariableBase(models.Model):
    select_related = []
    text_ng = models.ForeignKey(TextNG)
    label = models.CharField(
        _('label'), max_length=20,
        validators=[
            RegexValidator(
                regex='[_a-z]+',
                message=_('Only lower case characters.'))
        ]
    )

    def __unicode__(self):
        return self.label

    class Meta:
        abstract = True
        unique_together = ('text_ng', 'label')


class TextNGVariableText(TextNGVariableBase):
    value = models.TextField(_('value'), null=True, blank=True)

    class Meta:
        verbose_name = _('text')
        verbose_name_plural = _('texts')


class TextNGVariableFilerImage(TextNGVariableBase):
    value = FilerImageField(null=True, blank=True, verbose_name=_('value'))

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')


class TextNGVariableFilerFile(TextNGVariableBase):
    value = FilerFileField(null=True, blank=True, verbose_name=_('value'))

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')


class TextNGVariableHTML(TextNGVariableBase):
    value = HTMLField(null=True, verbose_name=_('value'))

    class Meta:
        verbose_name = _('html text')
        verbose_name_plural = _('html texts')


class TextNGVariableTextInput(TextNGVariableBase):
    value = models.CharField(max_length=1000, null=True, verbose_name=_('value'))

    class Meta:
        verbose_name = _('text input')
        verbose_name_plural = _('text inputs')
