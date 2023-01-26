from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Movie
from .serializer import MovieSerializer
from rest_framework import generics

# Create your views here.
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

