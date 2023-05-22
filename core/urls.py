from django.urls import path
from core import views
from .views import videoDetail

urlpatterns = [
    path("", views.home, name="home"),
    path("channel", views.channel, name="channel"),
    path("channel/videos", views.channel_videos, name="channel_videos"),
    path("channel/community", views.community, name="community"),
    path("channel/about", views.about, name="about"),
    path("video/<int:pk>", videoDetail, name="video_detail")
]