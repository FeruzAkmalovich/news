from django.db import models
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField()
    full_info = models.TextField(null=True)
    categories = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,related_name='categories')
    popular = models.IntegerField(default=1,null=True)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('post_detail_url',kwargs={'slug':self.slug})

    


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_detail_url',kwargs={'slug':self.slug})



class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='comments')
    author_name = models.CharField(max_length=255)
    comment_text = models.TextField(max_length=255)

    def __str__(self):
        return 'user:' + self.author_name + '--' + self.comment_text
    
