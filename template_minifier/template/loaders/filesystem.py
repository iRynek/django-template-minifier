"""
Wrapper for loading templates from the filesystem with stripping tags.
"""

from django.conf import settings
from django.template.loaders.filesystem import Loader as FilesystemLoader

from template_minifier.utils import get_template_minifier_strip_function


class Loader(FilesystemLoader):
    def get_contents(self, origin):
        contents = super(Loader, self).get_contents(origin)
        if getattr(settings, 'TEMPLATE_MINIFIER', True):
            return get_template_minifier_strip_function()(contents)
        else:
            return contents
