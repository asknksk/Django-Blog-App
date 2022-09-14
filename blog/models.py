from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog_image', blank=True, default="blog/images/default-img.jpg")    
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)
    blog_comment = models.PositiveIntegerField(default=0)
    blog_like=models.PositiveIntegerField(default=0)
    blog_view = models.IntegerField(default=0)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',blank=True)
    body = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.post.title}"