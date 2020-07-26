from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    # prepopulated_fields = {'slug': ('name', )}
    # search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
