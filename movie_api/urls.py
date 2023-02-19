from movie_api.views import MovieList, MovieDetail
from rest_framework.routers import DefaultRouter
from movie_api import views
from django.urls import path

#router = DefaultRouter()
#router.register(r'movies', views.MovieViewSet, basename='movie')
urlpatterns = [
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie_detail"),
    path("movies/", MovieList.as_view(), name="movie_list")
]
