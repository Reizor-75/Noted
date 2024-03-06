from .models import Theme

def set_theme(request):
  if request.user.is_authenticated:
    cur_theme = Theme.objects.filter(user = request.user).last()
    return { 'THEME': cur_theme.color }
  else:
    return { 'THEME': "NA" }

def set_font(request):
  if request.user.is_authenticated:
    cur_theme = Theme.objects.filter(user = request.user).last()
    return { 'FONT': cur_theme.font }
  else:
    return { 'FONT': "1" }