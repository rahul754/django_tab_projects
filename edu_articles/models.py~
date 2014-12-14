from django.db import models
from time import time


def get_upload_file_name(instance, filename):
   return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)

    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/articles/get/%i/" % self.id  
    



class Comment(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    article = models.ForeignKey(Article)


class CommentSecond(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    article = models.ForeignKey(Article)

