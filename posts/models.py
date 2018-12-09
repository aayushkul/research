from django.db import models
from branches.models import Journal

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=256)
    authors = models.TextField()
    summary = models.TextField()
    type = models.CharField(max_length=256)
    journal = models.ForeignKey(Journal,on_delete=models.CASCADE)
    link = models.URLField(null=True)
    date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
