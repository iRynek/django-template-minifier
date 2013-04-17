"""
Wrapper for loading templates from the filesystem with stripping tags.
"""

from django.conf import settings
from django.template.loaders.filesystem import Loader as FilesystemLoader

from template_minifier.utils import get_template_minifier_strip_function

class Loader(FilesystemLoader):
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
