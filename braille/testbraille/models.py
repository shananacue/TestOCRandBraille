from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Text(models.Model):
    test = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='images/')


    def __str__(self):
        return self.test 
    
    def get_absolute_url(self):
        return reverse('test-details', args=(str(self.id)))
    
