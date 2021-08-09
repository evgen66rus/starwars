from django.contrib import admin
from .models import Character, Planet, Notes

admin.site.register(Character)
admin.site.register(Planet)
admin.site.register(Notes)

class PlanetAdmin(admin.ModelAdmin):
   list_display = ("name")
   search_fields = ("name__startwith", )

class CharacterAdmin(admin.ModelAdmin):
   list_display = ("name")
   search_fields = ("name__startwith", )

class NotesAdmin(admin.ModelAdmin):
   list_display = ("name")