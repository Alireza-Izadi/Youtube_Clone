from django.shortcuts import render
from core.models import Video


# Create your views here.
def home(request):
    videos = Video.objects.filter(visibility="public")
    context = {
        "videos": videos,
    }
    return render(request, "index.html", context)

def channel(request):
    return render(request, "channel.html")

def channel_videos(request):
    return render(request, "channel-videos.html")

def community(request):
    return render(request, "community.html")

def about(request):
    return render(request, "about.html")