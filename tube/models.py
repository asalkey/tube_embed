from django.db import models

from embed_video.fields import EmbedVideoField

# Create your models here.

class Item(models.Model):
    video = models.URLField(max_length=100)

def __unicode__(self):
    return self.name
