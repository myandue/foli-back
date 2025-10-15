from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import QuizHistorySerializer
from .service import fetch_and_save_quiz_info


class QuizHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = QuizHistorySerializer(data=request.data)
        if serializer.is_valid():
            validated = serializer.validated_data
            quiz_data = fetch_and_save_quiz_info(
                user=request.user,
                keyword=validated["keyword"],
                level=validated["level"],
                amount=validated["amount"],
            )

            return Response(
                {"quiz_data": quiz_data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
