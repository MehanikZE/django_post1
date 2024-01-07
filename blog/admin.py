from django.contrib import admin

# Register your models here.
from blog.models import Post, Author_of_post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ('title', 'description', 'author', 'create_at', 'is_published', 'update_at')
admin.site.register(Author_of_post)
admin.site.register(Category)