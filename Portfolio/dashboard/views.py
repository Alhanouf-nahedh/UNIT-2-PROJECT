from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Project
from main.models import Message
from dashboard.forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def admin_only(user):
    return user.is_superuser

@login_required
@user_passes_test(admin_only)
def dashboard_view(request):
    """Dashboard view to list and manage projects."""
    projects = Project.objects.all()
    return render(request, 'dashboard/dashboard.html', {'projects': projects})

@login_required
@user_passes_test(admin_only)
def add_project_view(request):
    """View to add a new project."""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard_view')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/add_project.html', {'form': form})

@login_required
@user_passes_test(admin_only)
def edit_project_view(request, project_id):
    """View to edit an existing project."""
    try:
        # Try to retrieve the project by its ID
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        # If the project does not exist, redirect to the dashboard
        return redirect('dashboard:dashboard_view')

    # Handle form submission if the request method is POST
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard_view')
    else:
        # display the form with current project data
        form = ProjectForm(instance=project)
    
    return render(request, 'dashboard/edit_project.html', {'form': form, 'project': project})


@login_required
@user_passes_test(admin_only)
def delete_project_view(request, project_id):
    """View to delete a project."""
    try:
        project = Project.objects.get(id=project_id)
        project.delete()
    except Project.DoesNotExist:
        # If the project does not exist, redirect to the dashboard
        return redirect('dashboard:dashboard_view')

    return redirect('dashboard:dashboard_view')

@login_required
@user_passes_test(admin_only)
def manage_messages_view(request):
    """View to manage messages."""
    messages_list = Message.objects.all().order_by('-sent_at')
    return render(request, 'dashboard/manage_messages.html', {'messages_list': messages_list})



def delete_message_view(request, message_id):
    """View to delete a message."""
    try:
        message = Message.objects.get(id=message_id)
        message.delete()
    except Message.DoesNotExist:
        # If the message does not exist, redirect to the manage messages page
        return redirect('dashboard:manage_messages_view')

    return redirect('dashboard:manage_messages_view')