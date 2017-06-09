from celery import shared_task

from . import utils
from .backend import FreeIPABackend


def schedule_sync():
    """
    This function calls task only if it is not already running.
    The goal is to avoid race conditions during concurrent task execution.
    """
    if utils.is_syncing():
        return

    utils.renew_task_status()
    _sync_groups.apply_async(countdown=10)


@shared_task(name='waldur_freeipa.sync_groups')
def sync_groups():
    """
    This task is used by Celery beat in order to periodically
    schedule FreeIPA group synchronization.
    """
    schedule_sync()


@shared_task()
def _sync_groups():
    """
    This task actually calls backend. It is called asynchronously
    either by signal handler or Celery beat schedule.
    """
    FreeIPABackend().synchronize_groups()
