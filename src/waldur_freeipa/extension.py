from nodeconductor.core import NodeConductorExtension


class FreeIPAExtension(NodeConductorExtension):
    class Settings:
        WALDUR_FREEIPA = {
            'host': 'ipa.example.com',
            'username': 'admin',
            'password': 'secret',
            'verify_ssl': True,
            'username_prefix': '',
        }

    @staticmethod
    def django_app():
        return 'waldur_freeipa'

    @staticmethod
    def rest_urls():
        from .urls import register_in
        return register_in

