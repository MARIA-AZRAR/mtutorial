from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetListView.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetailView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view())
]