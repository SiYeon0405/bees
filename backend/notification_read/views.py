from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from notifications.models import Notification

class MarkAsReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            notification = Notification.objects.get(id=pk, user=request.user)
        except Notification.DoesNotExist:
            return Response({"error": "알림을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        notification.is_read = True
        notification.save()
        return Response({"message": "알림을 확인했습니다."}, status=status.HTTP_200_OK)


