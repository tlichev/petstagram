from django.db import models

from perstagram.photos.models import Photo


# Create your models here.

class Comment(models.Model):
    text = models.TextField()
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)



class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)