from django.urls import path
from .views import (
    AudioUploadView,
    TranscriptionView,
    SummaryView,
    QuizView,
    ConversationView,
)

urlpatterns = [
    path("upload-audio", AudioUploadView.as_view(), name="upload-audio"),
    path("transcript", TranscriptionView.as_view(), name="transcript"),
    path("summary", SummaryView.as_view(), name="summary"),
    path("quiz", QuizView.as_view(), name="quiz"),
    path("conversation", ConversationView.as_view(), name="conversation"),
]
