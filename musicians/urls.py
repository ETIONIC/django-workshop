from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from musicians import views

urlpatterns = [
    path('musicians/', views.MusicianList.as_view()),
    path('musicians/<int:pk>/', views.MusicianDetail.as_view()),
]
