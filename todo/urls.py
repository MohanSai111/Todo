from django.urls import path

from . import views

urlpatterns=[
   path('addtask/' ,views.addtask,name='add-task'),
]