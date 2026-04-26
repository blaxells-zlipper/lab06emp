from django.db import models
from django.utils.text import slugify  # NUEVO: Para generar slugs


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, help_text="Descripción opcional del género")  # NUEVO: Campo adicional
    slug = models.SlugField(blank=True)  # NUEVO: Para URLs amigables (sin unique por simplicidad)

    class Meta:
        db_table = "genres"
        ordering = ["name"]
        verbose_name = "genre"
        verbose_name_plural = "genres"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # NUEVO: Generar slug automáticamente
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    # Relación ManyToMany # NUEVO
    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )

    # Auditoría (muy importante en proyectos reales)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "movies"
        ordering = ["-created_at"]
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title