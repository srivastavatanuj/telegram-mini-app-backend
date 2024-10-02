"""
URL configuration for backend project.

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
from asyncio import tasks
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def root_view(request):
    return HttpResponse("Welcome to the API. Use /api/v1/user/ or /api/v1/task/ or /api/v1/invites/.")

# Health check view for Elastic Beanstalk health check
def health_check(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('users.urls')),
    path('api/v1/task/', include('tasks.urls')),
    path('api/v1/invites/', include('invites.urls')),
    path('', root_view),  # Add this line to handle the root URL
    path('health/', health_check),  # Health check URL for Elastic Beanstalk
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
