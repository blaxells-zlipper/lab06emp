from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'genres', GenreViewSet, basename='genre')
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet


urlpatterns = router.urls

urlpatterns = router.urls