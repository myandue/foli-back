from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .service import set_chat_context


class ChatView(APIView):
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        session_id = request.data.get("session_id")
        # session_id = f"user:{request.user.id}"
        context = request.data.get("context")
        if not session_id or not context:
            return Response(
                {"error": "session_id and context are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            set_chat_context(session_id=session_id, context=context)
            return Response(
                {"message": "Chat context set successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(e)
            return Response(
                {"error": "An error occurred while setting chat context."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
