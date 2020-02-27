from django.db import models

# Create your models here.

class RailwayJobsModel(models.Model):
    company = models.CharField(max_length=100)
    post_name = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    total_post = models.IntegerField()
    location = models.CharField(max_length=50)
    last_date = models.DateField(max_length=100)