from django.urls import path
from .views import InviteCreateView, InviteJoinView

urlpatterns = [
    path('', InviteCreateView.as_view(), name='invite-create'),  # 경로를 '' 로!
    path('join/', InviteJoinView.as_view(), name='invite-join'),
]
