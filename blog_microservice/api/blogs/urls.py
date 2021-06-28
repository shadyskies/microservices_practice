from django.urls import path
from .views import BlogViewset

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
]
