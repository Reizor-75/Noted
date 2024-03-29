from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('subjects/', views.note_subjects, name='subjects'),
  path('<subject>/notes/', views.note_index, name='note-index'),
  path('<subject>/notes/<int:note_id>/', views.note_detail, name='note-detail'),
  path('notes/create/', views.NoteCreate.as_view(), name='note-create'),
  path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note-update'),
  path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note-delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('theme/', views.view_theme, name='view-theme'),
  path('theme/<color>', views.set_theme, name='set-theme'),
  path('theme/font/<font>', views.set_font, name='set-font'),
]