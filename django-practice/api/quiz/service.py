import requests
import os

from .models import QuizHistory

AI_SERVER_URL = os.getenv("AI_SERVER_URL", "http://localhost:9000")


def fetch_and_save_quiz_info(user, keyword, level, amount):
    api_url = f"{AI_SERVER_URL}/api/quiz/keyword"
    params = {"keyword": keyword, "level": level, "amount": amount}

    response = requests.post(api_url, json=params)
    response.raise_for_status()

    quiz_data = response.json().get("questions", [])

    QuizHistory.objects.create(
        user=user, keyword=keyword, level=level, amount=amount
    )

    return quiz_data
