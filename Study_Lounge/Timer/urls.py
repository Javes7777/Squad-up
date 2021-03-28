from django.urls import path
from .views import TimerListView, TimerDetailView

app_name = 'Timer'

urlpatterns = [
    path('', TimerListView.as_view(), name='Timer-list'),
    path('<pk>/', TimerDetailView.as_view(), name='Timer-detail'),
]