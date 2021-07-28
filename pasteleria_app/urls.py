from django.urls import path
from pasteleria_app import views


urlpatterns = [
    path('pasteles/', views.pastel_api_view),
]
