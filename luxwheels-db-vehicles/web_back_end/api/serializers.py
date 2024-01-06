from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import User, Reservation


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # To make the password not visible
        # extra_kwargs = {'password': {'write_only': True, 'required': True}}


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
