from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    objects = models.Manager()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    image = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
