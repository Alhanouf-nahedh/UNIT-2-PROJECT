from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('logout/', views.logout_view, name='logout'),
    path('projects/add/', views.add_project_view, name='add_project_view'),
    path('projects/<int:project_id>/edit/', views.edit_project_view, name='edit_project_view'),
    path('projects/<int:project_id>/delete/', views.delete_project_view, name='delete_project_view'),
    path('messages/', views.manage_messages_view, name='manage_messages_view'),
]