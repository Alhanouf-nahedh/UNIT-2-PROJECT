from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Message

from django.contrib import messages

ADMIN_USERNAME = "Alhanouf"
ADMIN_PASSWORD = "ABC123"

def login_view(request):
    """View to handle user login."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect('dashboard:dashboard_view')  # Allow access to dashboard
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'main/login.html')


def home_view(request):
    return render(request, 'main/home.html')

def about_view(request):
    return render(request, 'main/about.html')

def contact_view(request):
    return render(request, 'main/contact.html')