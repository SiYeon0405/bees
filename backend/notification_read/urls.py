from django.urls import path
from .views import MarkAsReadView

urlpatterns = [
    path('<int:pk>/', MarkAsReadView.as_view(), name='mark-notification-read'),
]