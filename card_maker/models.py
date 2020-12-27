from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status = 'published')
        

class Post(models.Model):
	STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'), )
	title = models.CharField(max_length= 250)
	slug = models.SlugField(max_length=250) 
	author =models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')
	body = models.TextField() 
	publish = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft') 
	objects = models.Manager()
	published  = PublishedManager()

	def get_absolute_url(self):
		return reverse('card_maker:post_detail',args=[self.publish.year, self.publish.month,self.publish.day, self.slug])



class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

