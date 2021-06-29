from django.urls import path
from .views import BlogViewset, UserLoginView, UserRegisterView

urlpatterns = [
    path('blogs/', BlogViewset.as_view({
        'get': 'list',
        'post': 'create',

    })),
    path('blogs/<str:pk>', BlogViewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('login/', UserLoginView().as_view(), name='login'),
    path('register/', UserRegisterView().as_view(), name='register'),

]
