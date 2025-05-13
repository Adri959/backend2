from django.db import models
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName
    
class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    boxArt = models.ImageField(upload_to="images/")
    uploadDate = models.DateTimeField(default=now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    