from django.urls import path
from .views import AllWods, LikesView, UserLikesView, WodsView

urlpatterns = [
    path('all/', AllWods.as_view()),
    path('<int:id>/', WodsView.as_view()),
    path('likes/', LikesView.as_view()),
    path('likes/<int:id>/', LikesView.as_view()),
    path('likes/user/<int:id>/', UserLikesView.as_view())
]