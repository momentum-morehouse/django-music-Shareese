from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    released = models.DateField(blank=True, null=True)

    def __str__(self):
      return f"{self.title}"

