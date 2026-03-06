from django.urls import path

from . import views

urlpatterns=[
   path('addtask/' ,views.addtask,name='add-task'),
   path('mark_as_done/<int:pk>/',views.marks_as_done,name='mark-as-done'),
   path('mark_as_undone/<int:pk>/',views.marks_as_undone,name='mark-as-undone'),
   path('edit_task/<int:pk>/',views.edit_task,name='edit-task'),
   path('delete_task/<int:pk>/',views.delete_task,name='delete-task')
]