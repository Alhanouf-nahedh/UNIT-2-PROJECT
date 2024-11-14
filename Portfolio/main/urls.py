from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about_view, name='about_view'),
    path('contact/', views.contact_view, name='contact_view'),
]