from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length = 120)
	slug = models.SlugField(null = True,unique =False,blank = True) # 
	content = models.TextField(null= True,blank = True)
