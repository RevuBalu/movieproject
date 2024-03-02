from django.db import models

# Create your models here.
class Online(models.Model):
    image=models.ImageField(upload_to="online/images", null=True, blank=True)
    title=models.CharField(max_length=30,unique=True,primary_key=True)
    subtitle=models.CharField(max_length=30)
    year=models.IntegerField()
    def __str__(self):
      return self.title
