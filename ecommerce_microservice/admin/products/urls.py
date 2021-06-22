from .views import ProductViewset
from django.urls import path


urlpatterns = [
    path('products/', ProductViewset.as_view({
        'get': 'list',
        'post': 'create',

    })),
    path('products/<str:pk>/', ProductViewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
