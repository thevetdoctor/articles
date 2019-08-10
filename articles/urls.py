from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:id>/', views.article_detail),
    path('articles/<int:id>/edit/', views.article_edit),
    path('articles/<int:id>/delete/', views.article_delete),
    url('articles/', views.article_all),
    # url('/-*/redirect/', views.redirect_url),
    url('', views.home),
    # url('articles/<int:id>/', views.article_detail),
    # url(r'^articles/(?P<id>\d)/$', views.article_all),
    # url('', views.home),
]
