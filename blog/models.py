from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog_image', blank=True)    
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title