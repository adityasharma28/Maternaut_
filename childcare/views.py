from django.shortcuts import render
from scrapers import baby
import json
from django.http import JsonResponse

def childcare(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        babysitters = baby.get_babysitters(city)
        return JsonResponse(babysitters, safe=False)
    return render(request, 'childcare/childcare.html')


# def child_search(request):
#     city = request.POST.get('city')
#     print(city)
#     babysitters = baby.get_babysitters(city)
#     # babysitters = json.loads(babysitters)  
#     return JsonResponse(babysitters, safe=False)


