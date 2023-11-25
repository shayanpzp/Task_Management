from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
