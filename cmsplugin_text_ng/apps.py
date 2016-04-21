from django.apps import AppConfig

from cmsplugin_text_ng.type_registry import register_type


class CmsPluginTextNgConfig(AppConfig):
    name = 'cmsplugin_text_ng'
    verbose_name = "Django Cms Plugin Text-NG"

    def ready(self):
        from cmsplugin_text_ng import models
        register_type('text', models.TextNGVariableText)
        register_type('text_input', models.TextNGVariableTextInput)
        register_type('image', models.TextNGVariableFilerImage)
        register_type('file', models.TextNGVariableFilerFile)
        register_type('html_text', models.TextNGVariableHTML)
