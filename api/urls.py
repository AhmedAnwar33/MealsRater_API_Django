from django.urls import path,include
from rest_framework import routers
from .views import MealViewsets,RatingViewsets

router = routers.DefaultRouter()
router.register('mael',MealViewsets)
router.register('rating',RatingViewsets)

urlpatterns = [
    path('',include(router.urls)),
] 

# urlpatterns = [
#     path('meal',MealViewsets.as_view({'get': 'list'}),name='meal'),
#     path('rating',RatingViewsets.as_view({'get': 'list'}),name='rating')
# ] 