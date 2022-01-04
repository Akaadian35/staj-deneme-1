from django.contrib import admin
from mysite.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'slug', 'read']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']

    class Meta:
        model = Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "slug",
    )


admin.site.register(Post, PostAdmin)
