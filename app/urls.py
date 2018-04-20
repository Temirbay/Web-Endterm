from django.urls import path

from . import views

urlpatterns = [
    path ('blogs/', views.blog_list, name="blog_list"),
    path ('blogs/<int:blog_id>', views.blog_details, name="blog_details"),
    path ('blogs/update/<int:blog_id>', views.blog_update, name="blog_update"),
    path ('blogs/delete/<int:blog_id>', views.blog_delete, name="blog_delete"),
    path ('blogs/add/', views.blog_add, name="blog_add"),
]