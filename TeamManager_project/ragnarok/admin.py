from django.contrib import admin
from ragnarok.models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'likes']

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)


# Register your models here.
