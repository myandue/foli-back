import requests
from django.conf import settings

from .models import QuizHistory

AI_SERVER_URL = settings.AI_SERVER_URL


def fetch_and_save_quiz_info(user, keyword, level, amount):
    api_url = f"{AI_SERVER_URL}/api/quiz/keyword"
    params = {"keyword": keyword, "level": level, "amount": amount}

    # Mock data for testing without ai-server
    # response = {
    #     "questions": [
    #         {
    #             "question": f"{keyword} 관련 샘플 질문 1?",
    #             "answers": [
    #                 {"answer": "Answer A", "correct": True},
    #                 {"answer": "Answer B", "correct": False},
    #                 {"answer": "Answer C", "correct": False},
    #                 {"answer": "Answer D", "correct": False},
    #             ],
    #         },
    #         {
    #             "question": f"{keyword} 관련 샘플 질문 2?",
    #             "answers": [
    #                 {"answer": "Answer A", "correct": False},
    #                 {"answer": "Answer B", "correct": True},
    #                 {"answer": "Answer C", "correct": False},
    #                 {"answer": "Answer D", "correct": False},
    #             ],
    #         },
    #     ],
    # }

    response = requests.post(api_url, json=params)
    response.raise_for_status()

    quiz_data = response.json().get("questions", [])

    QuizHistory.objects.create(
        user=user, keyword=keyword, level=level, amount=amount
    )

    return quiz_data
