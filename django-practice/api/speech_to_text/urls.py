from django.urls import path
from .views import AudioUploadView, TranscriptionView, SummaryView, QuizView

urlpatterns = [
    path("upload-audio", AudioUploadView.as_view(), name="upload-audio"),
    path("transcribe", TranscriptionView.as_view(), name="transcribe"),
    path("summarize", SummaryView.as_view(), name="summarize"),
    path("quiz", QuizView.as_view(), name="quiz"),
]
