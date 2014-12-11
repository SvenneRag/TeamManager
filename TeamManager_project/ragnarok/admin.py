from django.contrib import admin
from ragnarok.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'likes']

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']

admin.site.register(Category, CategoryAdmin)
# admin.site.register(Page)
admin.site.register(Page, PageAdmin)

# Register your models here.
