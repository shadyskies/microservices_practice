from django.urls import path
from .views import register, base, user_quizzes, user_results
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', base, name='user-dashboard'),
    path('user-quizzes/', user_quizzes, name='user-quizzes'), 
    path('user-results/', user_results, name='user-results'),
]