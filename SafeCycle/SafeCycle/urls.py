
from django.contrib import admin
from django.urls import path

#Need to import views from the application so that they can be referenced
from application import views #these errors can be ignored

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('map/',views.map, name = 'map'),
    path('safety/',views.safety, name='safety'),
    path('reviews/choose/',views.reviews_home,name='reviews_home'),
    path('reviews/<int:road_id>/', views.reviews_detail, name='reviews_detail')
]
