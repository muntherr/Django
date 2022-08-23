from django.contrib import admin
from demo.models import Book

# Register your models here.
# admin.site.register(Book)
@admin.register(Book) # To change the view at the admin screen
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description'] # To hide some fields in the admin screen
    list_display = ['title' , 'description','price'] # To change the displayed option in the listed items
    list_filter = ['published']
    search_fields = ['title' , 'description']