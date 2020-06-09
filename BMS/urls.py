"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index,name='index'),
    url(r'^$',views.login,name='login'),
    url(r'^register/',views.reg,name='register'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^set_password',views.set_password,name='set_password'),
    url(r'^book/list/',views.book_list,name='book_list'),
    url(r'^book/add/',views.book_add,name='book_add'),
    url(r'^book/edit/(\d+)/',views.edit_book,name='edit_book'),
    url(r'^book/delete/(?P<delete_id>\d+)/',views.book_delete,name='book_delete')
]
