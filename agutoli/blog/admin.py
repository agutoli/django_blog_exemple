from agutoli import settings
from agutoli.blog.models import Post, Category
from django.contrib import admin

media = settings.MEDIA_URL

class PostAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'pub_date', 'text', 'keywords', 'published']
    class Media:
        js = ('plugins/tiny_mce/tiny_mce.js', 'admin/js/editor.js')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

