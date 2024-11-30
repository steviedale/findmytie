from django.contrib import admin
from .models import SearchQuery, Listing, QueryMatch

# Register your models here.
admin.site.register(SearchQuery)
admin.site.register(Listing)
admin.site.register(QueryMatch)