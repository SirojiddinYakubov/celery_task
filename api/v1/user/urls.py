from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('list/', views.UserListView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('update/<int:pk>/', views.UserUpdateView.as_view()),

    path('admin/create/', views.AdminCreateView.as_view()),
    path('admin/update/<int:pk>/', views.AdminUpdateView.as_view()),

    path('detail/<int:pk>/', views.UserDetailView.as_view()),
    path('delete/<int:pk>/', views.UserDeleteView.as_view()),
]
