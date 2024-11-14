from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects_list_view, name='projects_list_view'),
    path('<int:project_id>/', views.project_detail_view, name='project_detail_view'),
]
