from django.contrib import admin
from .models import Road, Reviews

@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ['name','rating']
    #pass

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['given_road','author']
    #pass

# Register your models here.
