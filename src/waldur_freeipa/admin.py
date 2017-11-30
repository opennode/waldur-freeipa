from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from waldur_core.core import admin as core_admin

from . import models, tasks


class ProfileAdmin(core_admin.ExtraActionsMixin, admin.ModelAdmin):
    list_display = ('username', 'user', 'is_active', 'agreement_date')
    readonly_fields = ('username', 'user', 'is_active', 'agreement_date')
    list_filter = ('is_active', )
    search_fields = ('username', )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_extra_actions(self):
        return [
            self.sync_groups,
        ]

    def sync_groups(self, request):
        tasks.schedule_sync()
        self.message_user(request, _('Groups synchronization has been scheduled.'))
        return redirect(reverse('admin:waldur_freeipa_profile_changelist'))


admin.site.register(models.Profile, ProfileAdmin)
