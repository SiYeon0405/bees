from rest_framework import serializers
from group_create.models import Document  # ✅ Document 모델 import

class DocumentSearchSerializer(serializers.ModelSerializer):
    """
    문서 검색 결과를 보여주기 위한 시리얼라이저.
    """
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'name', 'author_name', 'version', 'created_at']