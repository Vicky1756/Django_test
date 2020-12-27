
from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import filters
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import mixins
from .models import School, Student
from .serializers import  SchoolSerializer,StudentSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "location"]
    filterset_fields = ["name","max_student"]
    search_fields = ["name", "location"]
    ordering_fields = ["max_student"]

class StudentViewSet(viewsets.ModelViewSet):

    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])
    queryset = Student.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["school"]
    search_fields = ["firstname","lastname"]
    ordering_fields = ["firstname","lastname"]
    

def index(request):
    return HttpResponse('<a target="_blank" rel="noopenner noreferrer" href="https://github.com/jb-engine/challenges/tree/master/django">Click here for the documentation</a>')

