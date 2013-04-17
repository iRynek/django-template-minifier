"""
Wrapper for loading templates from "templates" directories in INSTALLED_APPS
packages with stripping tags.
"""

from django.conf import settings
from django.template.loaders.app_directories import Loader as AppDirectoriesLoader

from template_minifier.utils import get_template_minifier_strip_function

class Loader(AppDirectoriesLoader):
    def load_template_source(self, template_name, template_dirs=None):
        (source, filepath) = super(Loader, self).load_template_source(template_name, template_dirs)

        if getattr(settings, 'TEMPLATE_MINIFIER', True):
            return (
                get_template_minifier_strip_function()(source),
                filepath
            )
        else:
            return (
                source,
                filepath
            )
