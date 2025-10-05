"""
URL configuration for project project.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def health_check(request):
    return JsonResponse({
        "status": "healthy",
        "service": "Django API",
        "version": "1.0",
        "debug": False
    })

urlpatterns = [
    path('', health_check),
    path('api/health/', health_check),
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/', include('app.urls')),
]