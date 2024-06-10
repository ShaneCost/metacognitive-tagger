from django.urls import path
from .views import HomePageView, InstructionsPageView, TaggingPageView, save_data, ThanksPageView, ExpertReviewView, handle_selection

urlpatterns = [
    path('handle_selection/', handle_selection, name='handle_selection'),
    path("review/", ExpertReviewView.as_view(), name="review"),
    path("thanks/", ThanksPageView.as_view(), name="thanks"),
    path("save_data/", save_data, name="save_data"),
    path("tagging/", TaggingPageView.as_view(), name="tagging"),
    path("about/", InstructionsPageView.as_view(), name="instructions"),
    path("", HomePageView.as_view(), name="home"),
]