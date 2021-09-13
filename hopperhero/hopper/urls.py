from django.urls import path
from . import views

urlpatterns = [
    path('hopper/', views.WodList.as_view()),
]