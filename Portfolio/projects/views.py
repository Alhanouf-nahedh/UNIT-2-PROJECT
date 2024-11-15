from django.shortcuts import render, get_object_or_404
from dashboard.models import Project

def projects_list_view(request):
    """View to list all projects."""
    projects = Project.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': projects})

def project_detail_view(request, project_id):
    """View to show details of a single project."""
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})