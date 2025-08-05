from django.contrib import admin
from django.urls import path, include
from operations import views

urlpatterns = [
    path('',views.loginUser,name='loginuser'),
    path('signup',views.signup,name="signup"),
    path('home', views.home, name='home'),
    path('logout', views.logoutUser, name='logout'),
    path('student_create',views.student_create, name='student_create'),
    path('student_update/<int:pk>/', views.student_update, name='student_update'),
    path('student_delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('departmentadd',views.departmentAdd,name='departmentadd'),
]