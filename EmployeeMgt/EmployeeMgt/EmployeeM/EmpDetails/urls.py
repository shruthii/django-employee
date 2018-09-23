from django.urls import path, include
from EmpDetails import views

urlpatterns = [
    path(r'^$', views.AboutView.as_view(),name='about'),
    #path(r'^about/$', views.AboutView.as_view(), name='about'),
]
