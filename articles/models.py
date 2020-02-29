from django.db import models

class Article(models.Model):
    class Meta:
        #article does not need to be saved to db since it is being pulled from the API
       managed = False 
    uuid = models.CharField(max_length=200)
    promo = models.TextField()
    body = models.TextField()
    headline = models.CharField(max_length=300)
    publish_at = models.DateTimeField('date published')
    byline = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500)
    instruments = models.CharField(max_length=500)
    pitch_text = models.TextField()
    def __str__(self):
        return self.headline

class Comment(models.Model):
    article_uuid = models.CharField(max_length=200)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.comment_text

class ContentConfig(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    entry_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.key