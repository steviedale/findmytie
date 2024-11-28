from django.contrib import admin
from .models import SearchQuery, Listing

# Register your models here.
admin.site.register(SearchQuery)
admin.site.register(Listing)