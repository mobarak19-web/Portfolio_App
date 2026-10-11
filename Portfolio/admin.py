from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Skill,
    Project,
    Experience,
    Education,
    ContactMessage,
    CustomUser,
    Profile,
)


admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ContactMessage)
admin.site.register(Profile)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'email', 'full_name', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Portfolio Information', {
            'fields': ('full_name', 'profile_picture'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'full_name',
                'profile_picture',
                'password1',
                'password2',
            ),
        }),
    )