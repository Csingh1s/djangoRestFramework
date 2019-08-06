from rest_framework import serializers
from rbasis.serializers import *
from .models import *

class userSerializer(ShAPISerializer):
    class Meta:
        model = user
        fields = ("user_name", "email", "first_name", "last_name", "password")

class receiptSerializer(ShAPISerializer):
    class Meta:
        model = receipt
        fields = ("url", "name", "user_name")

class stepSerializer(ShAPISerializer):
    class Meta:
        model = step
        fields = ("text", "receipt")

class ingredientSerializer(ShAPISerializer):
    class Meta:
        model = ingredient
        fields = ("text", "receipt")

