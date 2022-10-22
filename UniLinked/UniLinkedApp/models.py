from django.db import models

# Create your models here.
class Register(models.Model):
    user = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 200)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.user
    
