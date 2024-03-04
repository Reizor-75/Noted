from django.shortcuts import render, redirect
from .models import Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def note_subjects(request):
  subjects = Note.objects.filter(user=request.user).values('subject')
  return render(request, 'subjects.html', { 'subjects': subjects })

def note_index(request, subject):
  notes = Note.objects.filter(user=request.user, subject=subject)
  return render(request, 'note/index.html', { 
    'subject':subject,
    'notes': notes })

def note_detail(request, subject, note_id):
  note = Note.objects.get(id=note_id)
  return render(request, 'note/detail.html', { 'note': note })

class NoteCreate(CreateView):
  model = Note
  fields = ['subject','title', 'date','key', 'content', 'summary']   
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/subjects/'

class NoteUpdate(UpdateView):
  model = Note
  fields = ['subject','title', 'date','key', 'content', 'summary']  

class NoteDelete(DeleteView):
  model = Note
  success_url = '/notes/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('subjects')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)