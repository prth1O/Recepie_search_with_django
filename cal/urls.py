from django.urls import path
from cal import views

urlpatterns=[
    path('recipe/',views.home,name='home'),


]
