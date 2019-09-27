from django.contrib import admin
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.admin import GroupAdmin, UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm, RoleAdminForm
from .models import User, Role

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    form = RoleAdminForm

    list_display = ('username', 'email', 'is_active')
    list_filter = ('admin', 'staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('groups',)}),
        # (None, {'fields': ('admin','staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email',)
    filter_horizontal = ('groups',)

    def get_form(self, request, obj=None, change=False, **kwargs):
        kwargs['labels'] = {'groups': 'Roles'}
        return super().get_form(request, obj=obj, change=change, **kwargs)

class UserInline(admin.TabularInline):
    model = User

class RoleInline(admin.TabularInline):
    model = Role

# # You also need to select_related because it will result in a bunch of SQL queries
# # @admin.register(Permission)
# # class PermissionAdmin(admin.ModelAdmin):
# #     def get_queryset(self, request):
# #         qs = super().get_queryset(request)
# #         return qs.select_related('content_type')

admin.site.register(User,UserAdmin)
admin.site.register(Role,GroupAdmin)
admin.site.register(Permission)
admin.site.unregister(Group)