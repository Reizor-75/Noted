from django.shortcuts import render
from .models import Note

# Create your views here.
def home(request):
  return render(request, 'home.html')

def notes_index(request):
  notes = Note.objects.all()
  return render(request, 'notes/index.html', { 'notes': notes })