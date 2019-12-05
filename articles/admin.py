from django.contrib import admin

# Register your models here.


from .models import Comment, ContentConfig

admin.site.register(Comment)
admin.site.register(ContentConfig)