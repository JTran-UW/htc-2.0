from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first', 'last', 'email', 'phone', 'rating', 'bio')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first', 'last', 'email', 'phone', 'bio', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['first'], 
            validated_data['last'], 
            validated_data['email'],
            validated_data['phone'],
            validated_data['bio'],
            validated_data['password']
        )

        return user
