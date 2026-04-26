from rest_framework import serializers
from django.utils import timezone
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "description", "slug"]  # NUEVO: Agregados description y slug
        read_only_fields = ["id", "slug"]  # NUEVO: slug es read-only

    def validate_name(self, value):  # NUEVO: Validación personalizada
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return value.strip()


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  # NUEVO: Serializer anidado para mostrar géneros completos

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "synopsis",
            "release_date",
            "duration_minutes",
            "is_active",
            "genres",  # NUEVO: Ahora muestra objetos completos
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_release_date(self, value):  # NUEVO: Validación para fecha no futura
        if value > timezone.now().date():
            raise serializers.ValidationError("La fecha de lanzamiento no puede ser futura.")
        return value

    def validate_duration_minutes(self, value):  # NUEVO: Validación para duración positiva
        if value <= 0:
            raise serializers.ValidationError("La duración debe ser mayor a 0 minutos.")
        return value