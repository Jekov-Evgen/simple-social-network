from django.urls import path, include
from .views import home_views

urlpatterns = [
    path('', home_views, name='home'),
]
