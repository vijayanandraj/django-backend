from movie_api.views import MovieViewSet
from rest_framework.routers import DefaultRouter
from movie_api import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
urlpatterns = router.urls