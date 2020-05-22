from django.urls import path, include

from .views import (
    api_detail_blog_view,
    api_update_blog_view,
    api_delete_blog_view,
    api_create_blog_view,
    # api_registration_view
)

app_name = 'api'

urlpatterns = [
    # blog views
    path('post/<int:pk>/', api_detail_blog_view, name='detail'),
    path('post/<int:pk>/update', api_update_blog_view, name='update'),
    path('post/<int:pk>/delete', api_delete_blog_view, name='delete'),
    path('post/create', api_create_blog_view, name='create'),
    
    # user views
    # path('user/register', api_registration_view, name='register'),
]
