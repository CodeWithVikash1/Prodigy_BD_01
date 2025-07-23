from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list.as_view(), name='user-list'),
    path('users/<uuid:id>/', views.user_detail.as_view(), name='user-detail'),
]