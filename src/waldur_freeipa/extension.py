from nodeconductor.core import NodeConductorExtension


class FreeIPAExtension(NodeConductorExtension):
    class Settings:
        WALDUR_FREEIPA = {
            'HOSTNAME': 'ipa.example.com',
            'USERNAME': 'admin',
            'PASSWORD': 'secret',
            'VERIFY_SSL': True,
            'USERNAME_PREFIX': '',
            'BLACKLISTED_USERNAMES': [],
        }

    @staticmethod
    def django_app():
        return 'waldur_freeipa'

    @staticmethod
    def rest_urls():
        from .urls import register_in
        return register_in

