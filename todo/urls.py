from django.urls import path
from .views import ListTodo , DetailTodo, TodoUpdateView


urlpatterns = [
    path('todos/', ListTodo.as_view()),
    path('todos/<int:pk>/', DetailTodo.as_view()),
    path('todos/<int:pk>/task_status/', TodoUpdateView.as_view()),
    path('todos/<int:pk>/delete/', TodoUpdateView.as_view()),
]