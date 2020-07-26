from django.urls import path
from . import views

urlpatterns = [
    path('id<int:user_id>/', views.view, name='user_profile_view'),
]