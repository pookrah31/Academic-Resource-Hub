from django.shortcuts import render
from rest_framework import generics
from .models import Material, Course
from .serializers import MaterialSerializer, CourseSerializer
# Create your views here.

class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def perform_create(self, serializer):
        #This links the upload to the logged-in student
        serializer.save(user=self.request.user)

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

