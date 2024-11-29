from django.db import models
import string
import random


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if not SearchQuery.objects.filter(code=code).exists():
            break
    return code


# Create your models here.
class SearchQuery(models.Model):
    code = models.CharField(max_length=50, unique=True, default=generate_unique_code)
    colors = models.CharField(max_length=1000, default='')
    host = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.colors}"

class Listing(models.Model):
    title = models.CharField(max_length=1000, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to ='images/') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.title}"

class QueryMatch(models.Model):
    search_query = models.ForeignKey(SearchQuery, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.search_query.code} - {self.listing.title}"