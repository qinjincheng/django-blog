from django.contrib import admin
from blogpost.models import Bolgpost

# Register your models here.

class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Bolgpost,BlogpostAdmin)