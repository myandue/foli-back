from django.urls import include, path

urlpatterns = [
    # path("auth/", include("api.auth.urls")),
    path("users/", include("api.users.urls")),
    path("quiz/", include("api.quiz.urls")),
    path("speech-to-text/", include("api.speech_to_text.urls")),
]
