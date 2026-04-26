from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Genre, Movie
from datetime import date


class GenreModelTest(TestCase):
    def test_genre_creation(self):  # NUEVO: Test básico para crear Genre
        genre = Genre.objects.create(name="Action", description="Películas de acción")
        self.assertEqual(genre.name, "Action")
        self.assertEqual(genre.slug, "action")
        self.assertEqual(str(genre), "Action")


class MovieModelTest(TestCase):
    def setUp(self):  # NUEVO: Configurar datos de prueba
        self.genre = Genre.objects.create(name="Drama")

    def test_movie_creation(self):  # NUEVO: Test para Movie con géneros
        movie = Movie.objects.create(
            title="Test Movie",
            synopsis="A test",
            release_date=date(2023, 1, 1),
            duration_minutes=120
        )
        movie.genres.add(self.genre)
        self.assertEqual(movie.title, "Test Movie")
        self.assertIn(self.genre, movie.genres.all())


class GenreAPITest(APITestCase):
    def test_create_genre(self):  # NUEVO: Test API para crear Genre
        url = reverse('genre-list')
        data = {"name": "Comedy", "description": "Películas divertidas"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Genre.objects.count(), 1)
        self.assertEqual(Genre.objects.get().name, "Comedy")


class MovieAPITest(APITestCase):
    def setUp(self):  # NUEVO: Configurar géneros para tests
        self.genre = Genre.objects.create(name="Sci-Fi")

    def test_create_movie(self):  # NUEVO: Test API para crear Movie
        url = reverse('movie-list')
        data = {
            "title": "Inception",
            "synopsis": "A mind-bending thriller",
            "release_date": "2010-07-16",
            "duration_minutes": 148,
            "is_active": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
