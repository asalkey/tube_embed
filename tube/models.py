from django.core.urlresolvers import reverse
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Item(models.Model):
    video = models.URLField(max_length=100)


    def get_absolute_url(self):
        return reverse('show-detail', kwargs={'pk': self.pk})

