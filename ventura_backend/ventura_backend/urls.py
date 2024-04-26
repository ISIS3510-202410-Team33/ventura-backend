"""
URL configuration for ventura_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from ventura import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('health-check/', views.health_check, name='health-check'),
    path('get_data/', views.get_data, name='get_data'),
    path('api/', include('ventura.api.urls')),
    path('download_top_3_edificios/', views.download_top_3_edificios, name='download_top_3_edificios'),
    path('download_keywords_for_edificios/', views.download_keywords_for_edificios, name='download_keywords_for_edificios')
]
