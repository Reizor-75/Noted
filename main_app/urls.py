from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('notes/', views.note_index, name='note-index'),
  path('notes/<int:note_id>', views.note_detail, name='note-detail'),
]