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
    color_1 = models.CharField(max_length=10, default="")
    color_2 = models.CharField(max_length=10, default="")
    color_3 = models.CharField(max_length=10, default="")
    host = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)