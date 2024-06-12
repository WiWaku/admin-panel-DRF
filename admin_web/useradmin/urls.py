from django.urls import path
from .views import UsersList, UsersDetail, Recruitment_View, ReferalView, ChannelList, ChatList

urlpatterns = [
    path('users/', UsersList.as_view()),
    path('users/<int:user_id>/', UsersDetail.as_view()),
    path('referal/<int:referal>/', ReferalView.as_view()),
    path('recruitment/<int:pk>', Recruitment_View.as_view()),
    path('chats/', ChatList.as_view()),
    path('channels/', ChannelList.as_view()),
    # path('statistics/', CheckStatistics.as_view()),
    ]
