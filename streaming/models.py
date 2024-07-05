from django.db import models

# Create your models here.
class shows(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    video_thumbnail=models.ImageField(upload_to='thumbnails', height_field=None, width_field=None, max_length=None)
    videos=models.FileField(upload_to='movies')
    category=models.CharField(max_length=100, null=True,blank=True)