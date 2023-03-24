from django.shortcuts import render
from django.http import Http404
# Create your views here.
from .models import Road

def home(request):
    roads = Road.objects.all()
    return render(request,'home.html',{
        'roads':roads,
    })

def map(request):
    roads = Road.objects.all()
    return render(request, 'map.html', {
        'roads': roads,
    })

def safety(request):
    return render(request, 'safety.html')

def reviews_home(request):
    roads = Road.objects.all()
    return render(request,'reviews_home.html',{
        'roads':roads,
    })

def reviews_detail(request, road_id):
    roads = Road.objects.all()
    try:
        road = Road.objects.get(id=road_id)
    except Road.DoesNotExist:
        raise Http404('road not found')
    return render(request, 'reviews_detail.html', {
        'road': road,'roads':roads
    })