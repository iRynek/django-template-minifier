"""
Wrapper for loading templates from "templates" directories in INSTALLED_APPS
packages with stripping tags.
"""

from django.conf import settings
from django.template.loaders.app_directories import Loader as AppDirectoriesLoader

from template_minifier.utils import get_template_minifier_strip_function


class Loader(AppDirectoriesLoader):
    def get_contents(self, origin):
        contents = super(Loader, self).get_contents(origin)
        if getattr(settings, 'TEMPLATE_MINIFIER', True):
            return get_template_minifier_strip_function()(contents)
        else:
            return contents
