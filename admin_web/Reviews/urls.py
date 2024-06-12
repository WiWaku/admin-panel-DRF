from django.urls import path
from .views import Reviews_View


urlpatterns = [
    path('rev/<int:pk>', Reviews_View.as_view()),
    ]
