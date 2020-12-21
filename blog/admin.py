from django.contrib import admin
from blog.models import Post, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display =('id', 'title', 'description', 'created')
    
    class Meta:
       model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass