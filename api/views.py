from rest_framework import viewsets
from .serializers import MealSerializers,RatingSerializers
from .models import Meal,Rating
# Create your views here.

class MealViewsets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers

class RatingViewsets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
