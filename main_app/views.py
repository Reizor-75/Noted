from django.shortcuts import render, redirect
from .models import Note, Theme
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

@login_required
def note_subjects(request):
  subjects = Note.objects.filter(user=request.user).values('subject').distinct()
  return render(request, 'subjects.html', { 'subjects': subjects })

@login_required
def note_index(request, subject):
  notes = Note.objects.filter(user=request.user, subject=subject).order_by('-date')
  return render(request, 'notes/index.html', { 
    'subject':subject,
    'notes': notes })

@login_required
def note_detail(request, subject, note_id):
  note = Note.objects.get(id=note_id)
  next_note = Note.objects.filter(user=request.user, subject=subject, date__lt=note.date).order_by('-date').first()
  return render(request, 'notes/detail.html', { 
    'note': note,
    'next' : next_note
  })

class NoteCreate(LoginRequiredMixin, CreateView):
  model = Note
  fields = ['subject','title', 'date','key', 'content', 'summary']   
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/subjects/'

class NoteUpdate(LoginRequiredMixin, UpdateView):
  model = Note
  fields = ['subject','title', 'date','key', 'content', 'summary']  

class NoteDelete(LoginRequiredMixin, DeleteView):
  model = Note
  success_url = '/subjects/'

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

@login_required
def view_theme(request):
  return render(request, 'change-style.html')

@login_required
def set_theme(request, color):
  cur_theme = Theme.objects.filter(user=request.user)
  if cur_theme.exists():
    user_theme = Theme.objects.get(user=request.user)
    user_theme.color = color
    user_theme.save()
  else:
    user_theme = Theme(user=request.user, color=color)
    user_theme.save()
  return redirect('view-theme')

@login_required
def set_font(request, font):
  cur_theme = Theme.objects.filter(user=request.user)
  if cur_theme.exists():
    user_theme = Theme.objects.get(user=request.user)
    user_theme.font = font
    user_theme.save()
  else:
    user_theme = Theme(user=request.user, font=font)
    user_theme.save()
  return redirect('view-theme')