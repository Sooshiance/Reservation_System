from django.contrib import admin

from club.models import FAQ, Rating


class FAQAdmin(admin.ModelAdmin):
    list_display = ('title',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(FAQ, FAQAdmin)

admin.site.register(Rating, RatingAdmin)
