from django.urls import path
from .views import MaterialListCreateView, CourseListView # Check these names!

urlpatterns = [
    path('materials/', MaterialListCreateView.as_view(), name='material-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
]