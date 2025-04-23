from django.shortcuts import render

# Create your views here.

def index(request):
    """Главная страница приложения "Пиццерия"."""
    return render(request, 'pizza_logs/index.html')
