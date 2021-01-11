from django.db import models
from django.conf import Settings, settings


class Post(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-created']
    
    

class Vote(models.Model):
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

