from django.shortcuts import render
from dashboard.models import Project

def projects_list_view(request):
    """View to list all projects."""
    projects = Project.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': projects})

def project_detail_view(request, project_id):
    """View to show details of a single project."""
    try:
        # Try to get the project by its ID
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        # If the project doesn't exist render the error page
        return render(request, 'projects/project_not_found.html', {'project_id': project_id})

    # If the project exists, render the detail page
    return render(request, 'projects/project_detail.html', {'project': project})