from __future__ import unicode_literals

from django.apps import AppConfig


class FreeIPAConfig(AppConfig):
    name = 'waldur_freeipa'
    verbose_name = 'FreeIPA'
    QUOTA_NAME = 'freeipa_quota'

    def ready(self):
        from nodeconductor.quotas.fields import QuotaField
        from nodeconductor.structure import models as structure_models

        structure_models.Customer.add_quota_field(
            name=self.QUOTA_NAME,
            quota_field=QuotaField()
        )

        structure_models.Project.add_quota_field(
            name=self.QUOTA_NAME,
            quota_field=QuotaField()
        )
