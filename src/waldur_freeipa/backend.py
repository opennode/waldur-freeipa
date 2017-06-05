from __future__ import unicode_literals

import python_freeipa

from django.conf import settings


class FreeIPABackend(object):
    def __init__(self):
        options = settings.WALDUR_FREEIPA
        self._client = python_freeipa.Client(
            host=options['HOSTNAME'],
            verify_ssl=options['VERIFY_SSL']
        )
        self._client.login(options['USERNAME'], options['PASSWORD'])

    def _format_ssh_keys(self, user):
        return list(user.sshpublickey_set.values_list('public_key', flat=True))

    def create_profile(self, profile):
        waldur_user = profile.user
        ssh_keys = self._format_ssh_keys(waldur_user)

        self._client.user_add(
            username=profile.username,
            first_name='N/A',
            last_name='N/A',
            full_name=waldur_user.full_name,
            mail=waldur_user.email,
            job_title=waldur_user.job_title,
            preferred_language=waldur_user.preferred_language,
            telephonenumber=waldur_user.phone_number,
            ssh_key=ssh_keys,
        )

    def disable_profile(self, profile):
        self._client.user_disable(profile.username)

    def enable_profile(self, profile):
        self._client.user_enable(profile.username)

    def update_ssh_keys(self, profile):
        ssh_keys = self._format_ssh_keys(profile.user)
        backend_profile = self._client.user_show(profile.username)
        if backend_profile['ipasshpubkey'] != ssh_keys:
            self._client.user_mod(profile.username, ipasshpubkey=ssh_keys)
