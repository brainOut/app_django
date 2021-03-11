from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, null=False)
    token = models.CharField(max_length=300, null=False)
    url = models.CharField(max_length=300, null=False)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project', kwargs={'slug': self.slug})
