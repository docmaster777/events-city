from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from user_profile import views as user_profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('user_profile.urls')),
    path('location/', include('location.urls')),
    path('object_user/', include('object_user.urls')),
    path('sign-in/', user_profile_views.sign_in, name='sign_in'),   #вход
    path('sign-up/', user_profile_views.sign_up, name='sign_up'),   #регистрация
    path('logout/', LogoutView.as_view(), {'next_page': '/'}, name='logout'),   #выход
    # path('logout/', logoutUser, name='logout'),
    # path('registration/', views.signup, name='registration'),
]
