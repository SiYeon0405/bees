from rest_framework import generics, filters, permissions
from .serializers import DocumentSearchSerializer
from group_create.models import Document

class DocumentSearchView(generics.ListAPIView):
    """
    문서 목록을 검색 및 필터링하는 API 뷰.
    이름(name), 작성자(author__username), 버전(version)으로 필터링 가능.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSearchSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'author__username', 'version']  # 검색 가능한 필드 목록
    ordering_fields = ['created_at', 'version']  # 정렬 필드 옵션 제공