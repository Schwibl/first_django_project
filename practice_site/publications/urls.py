from django.urls import path
from . import views

urlpatterns = [
    path('', views.publications_list, name='publications_list'),
    path('publications_item/<int:pk>/', views.publications_item_detail, name='publications_item')
] 