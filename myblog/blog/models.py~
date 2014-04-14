#coding: utf-8
from django.db import models



class Tag(models.Model):
      name = models.CharField(max_length=50)
      
      def __unicode__(self):
          return self.name


class Post(models.Model):
    title = models.CharField(max_length=255) 
    datetime = models.DateTimeField('Дата публикации')  
    content = models.TextField(max_length=10000)
    tag = models.ManyToManyField(Tag)    

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


#class Comment(models.Model):
#      post=models.ForeignKey(Post)
#      author=models.CharField(max_length=32)
#      text=models.TextField(max_length=100)
#        
#      def __unicode__(self):
#          return self.author

#      def get_absolute_url(self):
#          return "/blog/%i/" % self.id

