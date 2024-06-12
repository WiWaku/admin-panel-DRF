from django.urls import path
from .views import MeetingView, MeetingDetail, Append_user

urlpatterns = [
    path('', MeetingView.as_view()),
    path('<str:title>', MeetingDetail.as_view()),
    path('add_user/', Append_user),
    ]