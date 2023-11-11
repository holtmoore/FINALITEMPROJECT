from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
    