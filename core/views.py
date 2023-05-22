from django.shortcuts import render
from django.views.generic import DetailView
from core.models import Video, Comment
from channel.models import Channel
from .models import Video
from django.db.models import Count
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

def videoDetail(request, pk):
    video = Video.objects.get(id=pk)
    # channel = Channel.objects.get(user=video.user)
    
    # channel.total_views = channel.total_views + 1
    # channel.save()

    video.views = video.views + 1
    video.save()


    # Suggesting Video
    video_tags_id = video.tags.values_list("id", flat=True)
    similar_videos = Video.objects.filter(tags__in=video_tags_id).exclude(id=video.id)
    similar_videos = similar_videos.annotate(same_tags=Count("tags")).order_by("-same_tags", "-date")[:25]

    # Getting all comment related to a video
    comment = Comment.objects.filter(active=True, video=video).order_by("-date")

    context = {
        "video":video,
        # "channel":channel,
        "comment":comment,
        "similar_videos":similar_videos,
    }
    return render(request, "video_detail.html", context)

