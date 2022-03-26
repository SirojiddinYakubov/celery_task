from django.urls import path
from . import views

urlpatterns = [
    path('message/list/', views.MessageListView.as_view()),
    path('message/create/', views.MessageCreateView.as_view()),
    path('message/update/<int:pk>/', views.MessageUpdateView.as_view()),
    path('message/detail/<int:pk>/', views.MessageDetailView.as_view()),
    path('message/delete/<int:pk>/', views.MessageDeleteView.as_view()),
]
