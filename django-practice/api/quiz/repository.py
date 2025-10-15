from .models import QuizHistory


def save_quiz_history(user, keyword, level, amount):
    quiz_history = QuizHistory(
        user=user, keyword=keyword, level=level, amount=amount
    )
    quiz_history.save()
    return quiz_history
