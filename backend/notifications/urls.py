from django.urls import path
from .views import NotificationListView, MarkAsReadView
from .views import NotificationListView, MarkAsReadView, NotificationCreateView  # ← 추가됨

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/read/', MarkAsReadView.as_view(), name='notification-read'),
    path('create/', NotificationCreateView.as_view(), name='notification-create'),  # ← 추가됨
]
