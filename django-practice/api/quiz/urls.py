from django.urls import path
from .views import QuizHistoryView

urlpatterns = [
    path("quiz-data", QuizHistoryView.as_view(), name="quiz-data"),
]
