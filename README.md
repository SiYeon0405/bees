# 🐝 시연공주와 꿀벌들

**👩‍💻 개발자 중심 협업 웹 플랫폼**  
GitHub의 단점 보완 + Discord의 실시간 피드백 장점을 융합한  
**개발 협업을 위한 그룹 스페이스 웹**입니다.

---

## ✨ 주요 기능

- 🛡 **회원가입 / 로그인** (JWT 기반 인증)
- 🔗 **그룹 생성 및 참여** (초대코드 시스템)
- 📁 **파일 업로드 및 버전 관리**
- 💬 **댓글 / 알림 시스템**
- 🧑‍💼 **마이페이지**: 비밀번호 변경, 탈퇴 등

---

## 📌 프로젝트 개요

**Docverse**는 협업하는 개발자들이  
더욱 **안전하게**, **실시간으로**, **직관적으로** 일할 수 있도록 만든  
웹 기반 통합 협업 플랫폼입니다.

> ✅ 실시간 피드백 + 안전한 버전관리 + 편리한 그룹 초대  
> ✅ 백엔드 API와 프론트엔드 분리 구조 (협업 최적화)

---

## 🧪 구현한 핵심 기능

| 기능       | 설명                                                  |
|------------|-------------------------------------------------------|
| 회원가입   | 이메일, 비밀번호, 닉네임 입력 → JWT 토큰 발급        |
| 로그인     | 이메일 + 비밀번호로 JWT access / refresh 토큰 발급   |
| 마이페이지 | 정보 조회 및 수정 (닉네임, 자기소개, 프로필 이미지)   |
| 탈퇴       | JWT 인증 기반의 사용자 삭제 (is_active = False)      |
| 토큰 갱신  | refresh 토큰을 통해 access 토큰 재발급               |

---

## 🧩 DB 설계

총 **8개 테이블**로 구성된 MySQL 기반의 관계형 DB 사용  
2025년 5월 29일 기준, **100% 구현 및 마이그레이션 완료**


---

## ⚙️ 데이터베이스 초기화 방법

이 프로젝트는 `MySQL` 데이터베이스를 Docker 컨테이너로 운영하며, `bees_dump.sql` 덤프 파일을 통해 초기 데이터를 설정할 수 있습니다.  
아래 단계에 따라 데이터베이스를 복원해주세요.

---

### 1️⃣ 사전 준비

먼저 레포지토리를 클론하고 `backend` 디렉토리로 이동합니다.

```bash
git clone https://github.com/SiYeon0405/bees.git
cd bees/backend
```

---

### 2️⃣ Docker 컨테이너 실행

```bash
docker-compose up -d
```

- MySQL과 Django 서버 컨테이너가 백그라운드에서 실행됩니다.

---

### 3️⃣ 데이터베이스 초기화 (덤프 파일 복원)

초기 테이블과 샘플 데이터를 복원하려면 다음 명령어를 실행합니다:

```bash
docker exec -i django-mysql-db mysql -u root -p1234 bees_db < bees_dump.sql
```

- `bees_dump.sql` 파일은 `backend/` 디렉토리에 위치해야 합니다.
- root 비밀번호는 `1234`로 설정되어 있으며 `docker-compose.yml`에서 확인 가능합니다.

---

### 4️⃣ 컨테이너가 정상 실행 중인지 확인

```bash
docker ps
```

정상적으로 실행 중인 경우 예시:

```
CONTAINER ID   IMAGE       ...   PORTS                  NAMES
xxxxxx         bees-web    ...   0.0.0.0:8000->8000/tcp django-web
yyyyyy         mysql:8.0   ...   0.0.0.0:3307->3306/tcp django-mysql-db
```

---

### 5️⃣ Django Admin 페이지에서 데이터 확인

- 브라우저 접속: [http://localhost:8000/admin](http://localhost:8000/admin)
- 로그인 정보:

```
이메일: parksy03080916@gmail.com  
비밀번호: 팀장에게 문의
```

- 테이블 확인 가능: `users`, `files`, `comments`, `notifications` 등

---

### 🔁 6️⃣ 마이그레이션을 새로 하고 싶은 경우

모델을 수정한 경우 다음 명령어를 순차적으로 실행합니다:

```bash
# 1. 마이그레이션 생성
python manage.py makemigrations

# 2. 마이그레이션 적용
python manage.py migrate
```
