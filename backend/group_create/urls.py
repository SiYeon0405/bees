from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet  # ← 여기서 에러 났음

router = DefaultRouter()
router.register(r'', GroupViewSet)  # '' 또는 'group' 등 prefix

urlpatterns = [
    path('', include(router.urls)),
]
