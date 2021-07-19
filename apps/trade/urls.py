from django.urls import path

from apps.trade import views

urlpatterns = [
    path('', views.journal_list, name='journal_list'),
    path('add/', views.journal_create, name='journal_create'),
    path('update/<int:id>/', views.journal_update, name='journal_update'),
    path('delete/<int:id>/', views.journal_delete, name='journal_delete'),
]