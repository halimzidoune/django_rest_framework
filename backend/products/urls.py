from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailsAPIView.as_view())
]
