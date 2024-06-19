from django.urls import path
from .views import HomePageView, InstructionsPageView, TaggingPageView, save_data, ThanksPageView, ExpertReviewView, handle_selection, review_pt2, admin_only_view

urlpatterns = [
    path('admin-only/', admin_only_view, name='admin_only_view'),
    path("review_pt2/", review_pt2, name='review_pt2'),
    path("handle_selection/", handle_selection, name='handle_selection'),
    path("review/", ExpertReviewView.as_view(), name="review"),
    path("thanks/", ThanksPageView.as_view(), name="thanks"),
    path("save_data/", save_data, name="save_data"),
    path("tagging/", TaggingPageView.as_view(), name="tagging"),
    path("about/", InstructionsPageView.as_view(), name="instructions"),
    path("", HomePageView.as_view(), name="home"),
]