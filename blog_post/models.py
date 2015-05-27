from django.db import models
from user_accounts.models import Blogger

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length = 50)
	post = models.TextField()
	user = models.ForeignKey(Blogger)
	
	def __unicode__(self):
		return self.title