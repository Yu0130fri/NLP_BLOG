from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationForm
from blog.models import User
from .models.profile_models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
 
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'is_active',
                'is_admin',
            )
        })
    )
    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
 
    add_form = UserCreationForm  # adminでuser作成用に追加 
 
 
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)