from django.urls import path

from blog.views import blog, blog_detail


urlpatterns = [
    path('', blog, name='blog'),
    path('<str:slug>', blog_detail, name='blog_detail'),
]

