from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)
  date = models.DateField("Class Date")
  key = models.CharField(max_length=100)
  content = models.TextField(max_length=1000)
  summary = models.TextField(max_length=1000)  
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title}"

  def get_absolute_url(self):
    return reverse('note-detail', kwargs={
      'note_id': self.id,
      'subject': self.subject
      })

  def format_key(self):
    return self.key.split(", ")