from . import tasks, utils


def schedule_sync(*args, **kwargs):
    tasks.schedule_sync()


def schedule_sync_on_quota_change(sender, instance, created=False, **kwargs):
    if instance.name != utils.QUOTA_NAME:
        return
    if created and instance.limit == -1:
        return
    tasks.schedule_sync()
