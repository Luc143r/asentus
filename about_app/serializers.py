from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Latest_product
        fields = ('id', 'title', 'category', 'content')

class SubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'title', 'price', 'options1', 'options2', 'options3')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'vacancy')

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'name', 'email', 'message')