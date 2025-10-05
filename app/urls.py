from django.urls import path
from .views import (
    AirQualityAPIView, 
    SafetyScoreAPIView, 
    BestRouteAPIView, 
    NearestSafeLocationAPIView, 
    ComprehensiveSafetyAPIView, 
    WeatherAPIView, 
    AIAdviceAPIView,
    FutureAirQualityAPIView,  # تم تصحيح اسم الفئة
    FutureWeatherAPIView      # تم تصحيح اسم الفئة
)
from .healthcheck import health_check
urlpatterns = [
    path('air-quality/', AirQualityAPIView.as_view(), name='air_quality'),
    path('safety-score/', SafetyScoreAPIView.as_view(), name='safety_score'),
    path('best-route/', BestRouteAPIView.as_view(), name='best_route'),
    path('nearest-safe-location/', NearestSafeLocationAPIView.as_view(), name='nearest_safe_location'),
    path('comprehensive-safety/', ComprehensiveSafetyAPIView.as_view(), name='comprehensive_safety'),
    path('weather/', WeatherAPIView.as_view(), name='weather'),
    path('ai-advice/', AIAdviceAPIView.as_view(), name='ai_advice'),
    path('future-air-quality/', FutureAirQualityAPIView.as_view(), name='future_air_quality'),  # تم التصحيح
    path('future-weather/', FutureWeatherAPIView.as_view(), name='future_weather'),  # تم التصحيح
    path('health/', health_check, name='health_check'),  # إضافة مسار فحص الصحة
]