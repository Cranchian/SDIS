from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework import serializers

from .models import Prospect, Stock




class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"

class ProspectSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True, required=False)
    
    class Meta:
        model = Prospect
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user