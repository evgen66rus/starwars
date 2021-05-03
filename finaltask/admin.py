from django.contrib import admin
from .models import Character, Planet

admin.site.register(Character)
admin.site.register(Planet)

class PlanetAdmin(admin.ModelAdmin):
   list_display = ("name")
   search_fields = ("name__startwith", )

class CharacterAdmin(admin.ModelAdmin):
   list_display = ("name")
   search_fields = ("name__startwith", )