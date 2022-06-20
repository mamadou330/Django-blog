from django.contrib import admin

# Register your models here.
from posts.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated", )
    list_editable = ("published", )
    # template_name= "posts/index.html"


admin.site.register(BlogPost, BlogPostAdmin)