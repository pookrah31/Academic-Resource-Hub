from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'department', 'level')

    def create(self, validated_data):
        # This creates the user and handles password hashing (encryption)
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            department=validated_data.get('department', 'CS'),
            level=validated_data.get('level', 100)
        )
        return user