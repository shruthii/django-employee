"""EmployeeM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from EmpDetails import views
from django.contrib.auth import views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AboutView.as_view(), name='about'),
    #path('login/', vw.login, name='login'),
    path('signin/', views.CreateEmpDetailsView.as_view(), name='signin'),
    path('DraftListView/', views.DraftListView.as_view(), name='List'),
    path(r'^DraftListView/(?P<pk>\d+)/update/$', views.EmpDetailsUpdateView.as_view(), name='update'),


    path(r'accounts/logout/$', vw.login, name='logout', kwargs={'next_page':'/'}),
    #path(r'', include('EmpDetails.urls')),
]
