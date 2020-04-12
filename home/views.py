from django.shortcuts import render
from connect.models import user_info
from accounts.models import User
from django.http import JsonResponse

def home(request):
    return render(request, 'home/home.html')

def save_location(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        print(city, lat, lng)
        username = user_info.objects.filter(user=request.user)
        print(username)
        if len(username) == 0:
            print('true')
            instance = user_info()
            instance.user = request.user
            instance.location_lat = lat
            instance.location_lng = lng
            instance.city = city
            instance.save()
            return JsonResponse("{'status': 'ok'}", safe=False)
        else:
            print()
            instance = user_info.objects.get(user=request.user)
            instance.location_lat = lat
            instance.location_lng = lng
            instance.city = city
            instance.save()
            return JsonResponse("{'status': 'user found, updating details'}", safe=False)
        
