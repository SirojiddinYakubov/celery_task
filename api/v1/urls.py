from django.urls import path, include

urlpatterns = [
    path('common/', include('api.v1.common.urls')),
    path('user/', include('api.v1.user.urls')),
    path('task/', include('api.v1.task.urls')),
]
