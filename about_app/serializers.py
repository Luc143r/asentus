from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Latest_product
        fields = ("title", "category", "content")


class SubSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=150, read_only=True)
    price = serializers.IntegerField(read_only=True)
    options1 = serializers.CharField(read_only=True)
    options2 = serializers.CharField(read_only=True)
    options3 = serializers.CharField(read_only=True)

    class Meta:
        model = Subscription
        fields = ("title", "price", "options1", "options2", "options3")
        read_only_fields = fields


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ("name", "vacancy")


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ("name", "email", "message")
