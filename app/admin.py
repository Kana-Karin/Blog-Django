from django.contrib import admin
from .models import Memo

class MemoAdmin (admin.ModelAdmin):
    list_display = ('id','title','text','created_datatime','updated_datatime')
    list_display_links = ('id','title')

# Register your models here.
admin.site.register(Memo, MemoAdmin)