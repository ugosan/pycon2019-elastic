from django.contrib import admin

from myproject.models import Movie, Actor, Role


class ActorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']

admin.site.register(Actor, ActorAdmin)

class MovieAdmin(admin.ModelAdmin):
    ordering = ['-release_date']
    search_fields = ['title']
    list_display = ('title', 'tagline')


admin.site.register(Movie, MovieAdmin)


class RoleAdmin(admin.ModelAdmin):
    search_fields = ['role_name', 'movie__title', 'actor__name']
    list_display = ['role_name', 'movie_title', 'actor_name']
    
admin.site.register(Role, RoleAdmin)