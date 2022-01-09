from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(type='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(type='comedy')
    serializer_class = MovieSerializer
