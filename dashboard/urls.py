from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staffDetail, name='dashboard-staffDetail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.productDelete, name='dashboard-productDelete'),
    path('product/update/<int:pk>/', views.productUpdate, name='dashboard-productUpdate'),
    path('order/', views.order, name='dashboard-order')
]