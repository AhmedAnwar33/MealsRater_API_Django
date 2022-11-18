from django.contrib import admin
from . models import Meal,Rating
# Register your models here.
class MealAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    search_fields = ['title','description']
    list_filter = ['title']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['meal','user','start']
    list_filter = ['meal','user','start']

admin.site.register(Meal,MealAdmin)
admin.site.register(Rating,RatingAdmin)
