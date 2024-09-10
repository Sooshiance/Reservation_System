from django.contrib import admin

from user.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', "email")
    list_display_links = ('username', "email")


admin.site.register(Profile, ProfileAdmin)
