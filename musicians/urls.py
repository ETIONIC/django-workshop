from django.urls import path
from musicians import views

urlpatterns = [
    path('musicians/', views.musician_list),
    path('musicians/<int:pk>/', views.musician_detail),
]
