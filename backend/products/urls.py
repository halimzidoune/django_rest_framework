from django.urls import path
from . import views

urlpatterns = [
    #path('', views.ProductListCreateAPIView.as_view()),
    path('', views.ProductMixinView.as_view()),

    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    #path('<int:pk>/', views.ProductDetailsAPIView.as_view())
    path('<int:pk>/', views.ProductMixinView.as_view())


]
