from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Material, Course
from .serializers import MaterialSerializer, CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course__course_code', 'title'] # We filter by code or title

    def perform_create(self, serializer):
        #This links the upload to the logged-in student
        serializer.save(user=self.request.user)

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UpvoteMaterialView(APIView):
    permission_classes = [permissions.IsAuthenticated] # Only logged-in students can vote

    def post(self, request, pk):
        try:
            material = Material.objects.get(pk=pk)
            material.vote_count += 1
            material.save()
            return Response({"message": "Upvoted!", "new_count": material.vote_count}, status=status.HTTP_200_OK)
        except Material.DoesNotExist:
            return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)