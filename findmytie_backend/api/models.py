from django.db import models
import string
import random
import datetime


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
    created_at = models.DateTimeField(default=datetime.datetime.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.colors}"

class Listing(models.Model):
    # required fields
    title = models.CharField(max_length=1000)
    solid_color = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    retailer_url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to ='images/') 

    # TODO: change colors to required
    colors = models.CharField(max_length=200, blank=True)

    # optional fields
    color_description = models.CharField(max_length=200, blank=True)
    retailer_image_url = models.URLField(max_length=2000, blank=True)

    # metadata
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        N = 15
        if len(self.title) <= N:
            title = self.title
        else:
            title = self.title[:(N-3)] + '...'

        if type(self.color_description) is str and len(self.color_description) > 0:
            if len(self.color_description) <= N:
                color = self.color_description
            else:
                color = self.color_description[:(N-3)] + '...'
            return f"{self.id}: {title} - {color}"
        else:
            return f"{self.id}: {title}"

class QueryMatch(models.Model):
    search_query = models.ForeignKey(SearchQuery, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.id}: {self.search_query.code} - {self.listing.title}"