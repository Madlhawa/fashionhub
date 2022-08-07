from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name="home"),
    path('store/', views.store, name="store"),
    path('product/', views.product, name="product"),
]
