from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, "index.html")

def channel(request):
    return render(request, "channel.html")

def channel_videos(request):
    return render(request, "channel-videos.html")

def community(request):
    return render(request, "community.html")

def about(request):
    return render(request, "about.html")