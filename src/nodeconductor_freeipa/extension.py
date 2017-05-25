from nodeconductor.core import NodeConductorExtension


class FreeIPAExtension(NodeConductorExtension):
    class Settings:
        NODECONDUCTOR_FREEIPA = {
            'ENABLED': False,
            'host': 'localhost',
            'username': 'USERNAME',
            'password': 'PASSWORD',
            'verify_ssl': False,
        }

    @staticmethod
    def django_app():
        return 'nodeconductor_freeipa'

    @staticmethod
    def rest_urls():
        from .urls import register_in
        return register_in

