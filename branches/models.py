from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Journal(models.Model):
    name = models.CharField(max_length=256)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
