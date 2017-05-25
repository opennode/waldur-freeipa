from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from nodeconductor.core import serializers as core_serializers

from . import models


class ProfileSerializer(core_serializers.AugmentedSerializerMixin,
                        serializers.HyperlinkedModelSerializer):

    agree_with_policy = serializers.BooleanField(write_only=True,
                                                 help_text=_('User must agree with the policy.'))

    class Meta(object):
        model = models.Profile
        fields = ('uuid', 'username', 'agreement_date', 'is_active', 'agree_with_policy')
        protected_fields = ('username', 'agreement_date')
        read_only_fields = ('is_active',)

        extra_kwargs = dict(
            url={'lookup_field': 'uuid', 'view_name': 'freeipa-profile-detail'},
        )

    def validate_agree_with_policy(self, value):
        if not value:
            raise serializers.ValidationError(_('User must agree with the policy.'))

        return value

    def create(self, validated_data):
        user = self.context['request'].user
        if models.Profile.objects.filter(user=user).exists():
            raise serializers.ValidationError({'details': _('User already has profile.')})
        validated_data.pop('agree_with_policy')
        validated_data['user'] = user
        return super(ProfileSerializer, self).create(validated_data)
