from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name