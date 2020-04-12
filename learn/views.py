from django.shortcuts import render
from scrapers import youtube_crawl
import json
from django.http import JsonResponse

def learn(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        video_ids = youtube_crawl.youtube_crawler(query)
        return JsonResponse(video_ids, safe=False)
    return render(request, 'learn/learn.html')