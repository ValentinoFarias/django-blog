from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post
from .models import Comment

# Register your models here.



# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

