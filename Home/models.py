from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    images = models.ImageField(upload_to='static/images/')
    slug = models.SlugField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    def imageurl(self):
        if self.images and hasattr(self.images, 'url'):
            return self.images.url
     
    # def slug_value(self):
    #     return self.slug
