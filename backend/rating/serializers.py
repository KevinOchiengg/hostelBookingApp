from django.forms import ModelForm
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'comment','rate')
class ReviewForm(ModelForm):
    class Meta:
        model =  Rating
        fields = ('user', 'comment','rate', 'subject')