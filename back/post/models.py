from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.TextField(default="")
    discount_percent = models.TextField(default="")
    old_price = models.TextField(default="")
    new_price = models.TextField(default="")
    
    def __str__(self):
        return self.name
    