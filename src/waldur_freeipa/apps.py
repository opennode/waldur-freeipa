from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models import signals


class FreeIPAConfig(AppConfig):
    name = 'waldur_freeipa'
    verbose_name = 'FreeIPA'

    def ready(self):
        from nodeconductor.quotas.fields import QuotaField
        from nodeconductor.quotas import models as quota_models
        from nodeconductor.structure import models as structure_models
        from nodeconductor.structure import signals as structure_signals

        from . import handlers, utils

        for model in (structure_models.Customer, structure_models.Project):
            signals.post_save.connect(
                handlers.schedule_sync,
                sender=model,
                dispatch_uid='waldur_freeipa.handlers.schedule_sync_on_%s_creation' % model.__class__,
            )

            signals.pre_delete.connect(
                handlers.schedule_sync,
                sender=model,
                dispatch_uid='waldur_freeipa.handlers.schedule_sync_on_%s_deletion' % model.__class__,
            )

            structure_signals.structure_role_granted.connect(
                handlers.schedule_sync,
                sender=model,
                dispatch_uid='waldur_freeipa.handlers.schedule_sync_on_%s_role_granted' % model.__class__,
            )

            structure_signals.structure_role_revoked.connect(
                handlers.schedule_sync,
                sender=model,
                dispatch_uid='waldur_freeipa.handlers.schedule_sync_on_%s_role_revoked' % model.__class__,
            )

        signals.post_save.connect(
            handlers.schedule_sync_on_quota_change,
            sender=quota_models.Quota,
            dispatch_uid='waldur_freeipa.handlers.schedule_sync_on_quota_save',
        )

        structure_models.Customer.add_quota_field(
            name=utils.QUOTA_NAME,
            quota_field=QuotaField()
        )

        structure_models.Project.add_quota_field(
            name=utils.QUOTA_NAME,
            quota_field=QuotaField()
        )
