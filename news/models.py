from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    NEWS = 'news'
    SPORTS = 'sports'
    BUSINESS = 'business'
    ENTERTAINMENT = 'entertainment'
    TRAVEL = 'travel'

    CATEGORY_CHOICES = [
        (NEWS, 'News'),
        (SPORTS, 'Sports'),
        (BUSINESS, 'Business'),
        (ENTERTAINMENT, 'Entertainment'),
        (TRAVEL, 'Travel'),
    ]

    title = models.CharField(max_length=15, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class News_Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    overview = models.TextField(max_length=400)
    meta_keywords = models.TextField(max_length=400)
    thumbnail_url = models.URLField(max_length=1024)
    description = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    new_blog_slug = AutoSlugField(populate_from='title',unique=True, null=True, default=None )
    selected_home_post = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add= True)
    views_count = models.IntegerField(default=0)  # Added field for views count

    # def save(self, *args, **kwargs):
    #     self.thumbnail_url = self.convert_to_direct_link(self.thumbnail_url)
    #     super(News_Post, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('post',kwargs={
        'slug':self.new_blog_slug
        })
    
    def __str__(self):
        return self.title

   
  
    def increment_views(self):
        self.views_count += 1
        self.save()

   