from django.shortcuts import render
from .models import Note

# Create your views here.
def home(request):
  return render(request, 'home.html')

def note_index(request):
  notes = Note.objects.all()
  return render(request, 'note/index.html', { 'notes': notes })

def note_detail(request, note_id):
  note = Note.objects.get(id=note_id)
  return render(request, 'note/detail.html', { 'note': note })