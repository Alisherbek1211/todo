from django.urls import path
from .views import home,comuncom,deletetask,updatetask

urlpatterns = [
    path('',home),
    path('complete/<int:id>/',comuncom),
    path('delete/<int:id>/',deletetask),
    path('update/<int:id>/',updatetask),
]