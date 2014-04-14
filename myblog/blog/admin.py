from django.contrib import admin
from blog.models import Post, Tag #,Comment

admin.site.register(Post)
#admin.site.register(Comment)
admin.site.register(Tag)




# Register your models here.
