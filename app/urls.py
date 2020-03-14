 # -*- coding: utf-8 -*-

from django.urls import path
from . import views
urlpatterns=[
           path('',views.HomePageView.as_view(),name="home"),
           path('spage1/<int:pk>',views.spage1View.as_view(),name = 'spage1'),
           path('search/',views.search,name="search"),
           path('student/create',views.CreateStudent.as_view(),name = "create"),
           path('student/create/success/',views.success,name = "success"),
           path('student/update/<int:pk>',views.UpdateStudent.as_view(),name = "update"),
           path('signup/',views.SignUpView.as_view(),name = "signup"),
            path('student/delete/<int:pk>',views.DeleteStudent.as_view(),name = "delete"),
           ]
