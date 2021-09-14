from django.urls import path
from hopper import views

urlpatterns = [
    path('all/', views.get_all_wod),
    path('', views.user_wod)
]