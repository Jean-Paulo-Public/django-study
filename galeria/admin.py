from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "title", "text")
    list_display_links = ("id", "title")
    search_fields = ("title",)

admin.site.register(Fotografia, ListandoFotografias)
