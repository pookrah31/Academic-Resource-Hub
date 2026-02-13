from django.contrib import admin
from .models import Course, Material
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # This makes the list view show both the code and the name
    list_display = ('course_code', 'course_name')
    search_fields = ('course_code', 'course_name')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    # This shows the title, the linked course, and the student who uploaded it
    list_display = ('title', 'course', 'user', 'vote_count')
    list_filter = ('course',)
    search_fields = ('title',)