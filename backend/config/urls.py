from django.contrib import admin
from django.urls import path, include

# JWT 기반 로그인 / 리프레시 뷰
from users.views import EmailTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # ✅ Django 관리자 페이지
    path('admin/', admin.site.urls),

    # ✅ JWT 로그인 / 리프레시 토큰 발급
    path('api/auth/login/', EmailTokenObtainPairView.as_view(), name='jwt_login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='jwt_token_refresh'),

    # ✅ 사용자 관련 API 엔드포인트
    path('api/users/', include('users.urls')),
]
