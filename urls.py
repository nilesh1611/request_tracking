
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include, path
urlpatterns = [
    path('submit_request/', views.submit_request, name='submit_request'),
    path('request_tracking/', views.request_tracking, name='request_tracking'),
]