from django.contrib import admin
from django.urls import path, include

# JWT 기반 로그인 / 리프레시 뷰
from users.views import EmailTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # ✅ Django 관리자 페이지
    path('admin/', admin.site.urls),

    # ✅ JWT 로그인 및 토큰 갱신
    path('api/auth/login/', EmailTokenObtainPairView.as_view(), name='jwt_login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='jwt_token_refresh'),  # 🔄 정식 경로로 수정

    # ✅ 사용자 관련 API (회원가입, 마이페이지, 비밀번호 변경, 탈퇴 등)
    path('api/users/', include('users.urls')),
]
