from django.urls import path
from .views import InviteJoinView

urlpatterns = [
    path('join/', InviteJoinView.as_view(), name='invite-join'),