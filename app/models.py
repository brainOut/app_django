from django.db import models
from django.urls import reverse

ENTITIES = (
    ('brute_forcer', 'Brute Force'),
    ('fuzz', 'Fuzzing'),
)

ATTRIBUTES = (
    ("Fuzzing", (
        ('url', 'URL'),
        ('port', 'PORT')
    )),
    ("Brute Force", (
        ('url', 'URL'),
        ('filename', 'File Name'),
        ('target', 'Success Pattern')
    ))
)


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


class PenTest(models.Model):
    entity = models.CharField(
       max_length=50,
       choices=ENTITIES,
   )
    attr = models.CharField(
       max_length=50,
       choices=ATTRIBUTES,
   )
    value = models.CharField(max_length=100)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tests"
    )
