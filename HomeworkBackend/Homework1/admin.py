from django.contrib import admin

from . import models


class PokemonTrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'level', 'catch_date', 'trainer')
    list_filter = (['name'])
    search_fields = (['name', 'type'])
    sortable_by = (['name'])




admin.site.register(models.Pokemon, PokemonAdmin)
admin.site.register(models.PokemonTrainer, PokemonTrainerAdmin)
