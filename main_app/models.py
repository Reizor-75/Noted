from django.db import models
from datetime import date, datetime    
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Theme(models.Model):  
  user = models.ForeignKey(User, on_delete=models.CASCADE)  
  color = models.CharField(max_length=100)
  font = models.CharField(max_length=1)
  
  def __str__(self):
    return f"{self.color}"

class Note(models.Model):
  title = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)
  date = models.DateField("Class Date", default=datetime.now)
  key = models.TextField(blank=True, default='')
  content = models.TextField(blank=True, default='')
  summary = models.TextField(blank=True, default='')  
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title}"

  def get_absolute_url(self):
    return reverse('note-detail', kwargs={
      'note_id': self.id,
      'subject': self.subject
      })

  def format_key(self):
    return self.key.split(" ")