from django.core.cache import cache

QUOTA_NAME = 'freeipa_quota'


class TaskStatus(object):
    def __init__(self, cache_key):
        self.cache_key = 'waldur_freeipa_syncing_' + cache_key

    def is_syncing(self):
        """
        This function checks if task is already running.
        """
        return cache.get(self.cache_key)

    def renew_task_status(self):
        """
        This function sets lock with timeout. Lock is valid only for 1 minute.
        Then it should be renewed. Otherwise, lock is released.
        """
        cache.set(self.cache_key, True, 60)

    def release_task_status(self):
        cache.set(self.cache_key, False)
