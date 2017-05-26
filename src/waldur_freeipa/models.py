from __future__ import unicode_literals

import re

from django.conf import settings
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from nodeconductor.core import models as core_models


class Profile(core_models.UuidMixin, models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    username = models.CharField(
        _('username'), max_length=255, unique=True,
        help_text=_('Letters, numbers and ./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[a-zA-Z0-9_.][a-zA-Z0-9_.-]*[a-zA-Z0-9_.$-]?$'),
                                      _('Enter a valid username.'), 'invalid')
        ])
    agreement_date = models.DateTimeField(_('agreement date'), default=timezone.now,
                                          help_text=_('Indicates when the user has agreed with the policy.'))
    is_active = models.BooleanField(_('active'), default=True)
