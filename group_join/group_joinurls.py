from rest_framework.routers import DefaultRouter
from .views import GroupJoinViewSet

router = DefaultRouter()
router.register(r'join', GroupJoinViewSet)

urlpatterns = router.urls
