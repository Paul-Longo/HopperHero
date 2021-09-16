from django.urls import path
from users import views

urlpatterns = [
    path('all/', views.get_all_users),
    path('users/<int:id>/', views.get_user),
]
