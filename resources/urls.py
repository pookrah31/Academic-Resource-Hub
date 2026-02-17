from django.urls import path
from .views import MaterialListCreateView, CourseListView, UpvoteMaterialView # Check these names!

urlpatterns = [
    path('materials/', MaterialListCreateView.as_view(), name='material-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('materials/<int:pk>/upvote/', UpvoteMaterialView.as_view(), name='upvote-material'),
]