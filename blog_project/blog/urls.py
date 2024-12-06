from django.urls import path
from .views import detect_country_view, filter_blog_posts_view

urlpatterns = [
    path('', detect_country_view, name='index'),
    path('filter/', filter_blog_posts_view, name='filter_blog_posts'),
]