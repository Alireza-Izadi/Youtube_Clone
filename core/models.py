from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings

User = settings.AUTH_USER_MODEL
VISIBILITY = (
    ("private", "Private"),
    ("public", "Public"),
    ("unlisted", "Unlisted"),
    ("members_only", "Members Only"),
)
# Create your models here.
def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

class Video(models.Model):
    video = models.FileField(upload_to=user_directory_path)
    image =models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    tag = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    visiblity = models.CharField(choices=VISIBILITY, max_length=100, default="public")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title