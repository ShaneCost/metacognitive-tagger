from django.urls import path
from .views import HomePageView, InstructionsPageView, TaggingPageView, save_data, ThanksPageView

urlpatterns = [
    path("thanks/", ThanksPageView.as_view(), name="thanks"),
    path("save_data/", save_data, name="save_data"),
    path("tagging/", TaggingPageView.as_view(), name="tagging"),
    path("about/", InstructionsPageView.as_view(), name="instructions"),
    path("", HomePageView.as_view(), name="home"),
]