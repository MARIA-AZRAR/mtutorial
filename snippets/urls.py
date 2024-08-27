from django.urls import path
from snippets import views

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetListView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetailView.as_view(), name='snippet-detail'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),

]