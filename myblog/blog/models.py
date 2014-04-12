#coding: utf-8
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255) 
    datetime = models.DateTimeField('Дата публикации')  
    content = models.TextField(max_length=10000)
    

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


class Comment(models.Model):
	post=models.ForeignKey(Post)
	author=models.CharField(max_length=32)
	text=models.TextField(max_length=100)


 
   # def __unicode__(self):
    #    return self.text



    
