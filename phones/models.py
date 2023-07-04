from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.URLField(max_length=2000)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True)
