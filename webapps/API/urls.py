from django.urls import path
from .views import TranslateWordView, TranslateSentenceView, TranslateSubmissionView

urlpatterns = [
    path('translate/word/', TranslateWordView.as_view()),
    path('translate/sentences/', TranslateSentenceView.as_view()),
    path('translate/submission/', TranslateSubmissionView.as_view())
]