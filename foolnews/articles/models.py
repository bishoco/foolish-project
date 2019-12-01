from django.db import models


class Article(models.Model):
    class Meta:
        #article does not need to be saved to db since it is being pulled from the API
       managed = False 
    promo = models.TextField()
    body = models.TextField()
    headline = models.TextField()
    publish_at = models.DateTimeField('date published')
    byline = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500)