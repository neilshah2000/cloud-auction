from django.shortcuts import render
from rest_framework import viewsets
from .models import Movies
from .serializers import MoviesSerializer

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
