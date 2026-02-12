from rest_framework import serializers
from .models import Material, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_code', 'course_name']

class MaterialSerializer(serializers.ModelSerializer):
    # These lines help show names instead of just ID numbers
    course_name =serializers.ReadOnlyField(source='course.course_name')
    uploader_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Material
        fields = ['id', 'title', 'file_url', 'vote_count', 'user', 'course', 'course_name', 'uploader_name'] 
        read_only_fields = ['user', 'vote_count']


        