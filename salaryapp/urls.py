from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('salary/',views.salary,name='salary'),
    path('predict/',views.predire,name='predire')
]