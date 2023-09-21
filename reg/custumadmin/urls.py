from django.contrib import admin
from django.urls import path,include
from . import views
from django.urls import reverse


# app_name = 'custumadmin'


urlpatterns = [
    path('', views.adminlogin,name='adminlogin'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<str:id>/',views.delete,name='delete'),
    path('logout/', views.logout_view, name='logout'),

]