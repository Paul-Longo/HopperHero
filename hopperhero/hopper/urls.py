from django.urls import path
from hopper import views

urlpatterns = [
    path('all/', views.get_all_wod),
    path('<int:id>/', views.get_wod),
    path('likes/<int:id>/', views.get_likes)
]