from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import SpeechToTextSerializer
from .service import (
    process_audio_transcription,
    process_audio_summary,
    process_audio_quiz,
)


class AudioUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = SpeechToTextSerializer(data=request.data)
        if serializer.is_valid():
            speech_to_text_instance = serializer.save(user=request.user)
            return Response(
                {"id": speech_to_text_instance.id},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        speech_to_text_id = request.data.get("id")
        if not speech_to_text_id:
            return Response(
                {"error": "ID is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            transcription = process_audio_transcription(speech_to_text_id)
            return Response(
                {"transcription": transcription},
                status=status.HTTP_200_OK,
            )
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred while processing."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        speech_to_text_id = request.data.get("id")
        if not speech_to_text_id:
            return Response(
                {"error": "ID is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            summary = process_audio_summary(speech_to_text_id)
            return Response(
                {"summary": summary},
                status=status.HTTP_200_OK,
            )
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred while processing."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class QuizView(APIView):
    LEVEL = 1  # Default level
    AMOUNT = 5  # Default amount

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        speech_to_text_id = request.data.get("id")
        if not speech_to_text_id:
            return Response(
                {"error": "ID is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            quiz = process_audio_quiz(
                speech_to_text_id, self.LEVEL, self.AMOUNT
            )
            return Response(
                {"quiz": quiz},
                status=status.HTTP_200_OK,
            )
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred while processing."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
