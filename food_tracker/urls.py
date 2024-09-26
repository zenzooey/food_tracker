"""
URL configuration for food_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, reverse_lazy
from django.conf.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(('food.urls', 'food'), namespace="food")),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='auth_login'),
    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(next_page='food:login'), name='auth_logout'),
    re_path(r'^accounts/password/change$', auth_views.PasswordChangeView.as_view(template_name='password_change.html',success_url=reverse_lazy('food:login')),name='auth_password_change'),


]
