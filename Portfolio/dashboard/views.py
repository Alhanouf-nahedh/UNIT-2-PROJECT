from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Project
from main.models import Message
from dashboard.forms import ProjectForm
from django.contrib import messages
from main.views import ADMIN_USERNAME, ADMIN_PASSWORD


def logout_view(request):
    """Log out the user by redirecting to the login page."""
    # Simply redirect to the login page without clearing any sessions
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


def dashboard_view(request):
    """Dashboard view that only the admin can access."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the credentials match the admin credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            projects = Project.objects.all()
            return render(request, 'dashboard/dashboard.html', {'projects': projects})
    
    # If credentials are wrong or it's a GET request
    messages.error(request, 'Please log in as admin to access the dashboard.')
    return redirect('main:login')



def add_project_view(request):
    """View to add a new project from the dashboard."""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project added successfully!")
            return redirect('dashboard:manage_projects_view')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/add_project.html', {'form': form})

def edit_project_view(request, project_id):
    """View to edit an existing project."""
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully!")
            return redirect('dashboard:manage_projects_view')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dashboard/edit_project.html', {'form': form, 'project': project})

def delete_project_view(request, project_id):
    """View to delete a project from the dashboard."""
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, "Project deleted successfully!")
    return redirect('dashboard:manage_projects_view')

def manage_messages_view(request):
    return render(request, 'dashboard/manage_messages.html')
