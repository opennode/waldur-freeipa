from __future__ import unicode_literals

from django.apps import AppConfig


class FreeIPAConfig(AppConfig):
    name = 'nodeconductor_freeipa'
    verbose_name = 'FreeIPA'

    def ready(self):
        pass
