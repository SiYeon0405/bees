# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('users.urls')),
=======
    path('', include('users.urls')),  # ✅ users 앱의 URL 연결
>>>>>>> b8481a2 (feat: 회원가입 기능 복구 및 정상 작동 확인)
]