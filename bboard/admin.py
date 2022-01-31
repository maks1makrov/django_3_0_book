from django.contrib import admin

from bboard.models import Bd, Rubric


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'price')


admin.site.register(Bd, BdAdmin)
admin.site.register(Rubric)
