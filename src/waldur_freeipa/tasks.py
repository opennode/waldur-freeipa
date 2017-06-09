from celery import shared_task

from .backend import FreeIPABackend


@shared_task(name='waldur_freeipa.sync_groups')
def sync_groups():
    FreeIPABackend().synchronize_groups()
