from rest_framework import serializers
from .models import Rating,Meal

class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','title','description')
        
class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','meal','user','start')
