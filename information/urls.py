from django.urls import path
from .views import about_us , ContactFormView

app_name = 'info'

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name="contact"),
    path('', about_us, name="about"),    
]