from django.db import models
from .models import Movie


def slider_movies(request):
    movies = Movie.objects.all().order_by('title')[0:3]
    # movies = Movie.objects.last()
    return {'movie_slider': movies}