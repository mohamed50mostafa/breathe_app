# In your_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
import os

@api_view(['GET'])
def health_check(request):
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        return Response({
            "status": "healthy",
            "database": "connected",
            "environment": os.environ.get('RAILWAY_ENVIRONMENT', 'development')
        })
    except Exception as e:
        return Response({
            "status": "unhealthy",
            "error": str(e)
        }, status=500)