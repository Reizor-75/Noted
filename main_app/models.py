from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
  title: models.CharField(max_length=100)
  subject: models.CharField(max_length=100)
  date: models.DateField("Creation Date")
  key: models.CharField(max_length=100)
  content: models.TextField(max_length=1000)
  summary: models.TextField(max_length=1000)  
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.Title} "