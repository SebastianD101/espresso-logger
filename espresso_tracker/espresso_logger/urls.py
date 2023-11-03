from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_logs, name='coffee_logs'),
    path('add/', views.add_coffee_log, name='add_coffee_log'),
    path('delete/<int:log_id>/', views.delete_coffee_log, name='delete_coffee_log'),
]
