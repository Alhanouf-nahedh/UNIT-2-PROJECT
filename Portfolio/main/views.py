from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Message
from django.contrib import messages


def home_view(request):
    """Render the Home page."""
    return render(request, 'main/home.html')

def about_view(request):
    """Render the About page."""
    return render(request, 'main/about.html')

def contact_view(request):
    """
    Handle contact form submissions:
    - Save valid form data and show success message.
    - Render the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message!')
            return redirect('main:contact_view')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})