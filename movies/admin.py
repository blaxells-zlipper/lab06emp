from django.contrib import admin
from .models import Movie, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "slug")  # NUEVO: Agregados description y slug
    search_fields = ("name", "description")  # NUEVO: Búsqueda en description
    prepopulated_fields = {"slug": ("name",)}  # NUEVO: Auto-generar slug desde name
    ordering = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_genres", "release_date", "is_active")  # NUEVO: Cambiado 'genre' a 'get_genres'
    list_filter = ("is_active", "genres", "release_date")  # NUEVO: Cambiado 'genre' a 'genres'
    search_fields = ("title", "synopsis")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

    def get_genres(self, obj):  # NUEVO: Método para mostrar géneros en list_display
        return ", ".join([genre.name for genre in obj.genres.all()])
    get_genres.short_description = "Genres"