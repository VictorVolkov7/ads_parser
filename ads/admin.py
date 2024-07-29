from django.contrib import admin

from ads.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Register ad's model in django admin.
    """
    list_display: tuple = ('ad_id', 'title', 'author', 'views', 'position',)
    search_fields: tuple = ('ad_id', 'title', 'author', 'position')
