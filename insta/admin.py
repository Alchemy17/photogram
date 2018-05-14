from django.contrib import admin
from .models import Image, Profile, Comment
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    
    def get_location(self, instance):
        return instance.profile.user
    get_location.short_description = 'User'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)