from django.urls import path
from . import views


app_name = 'collegeproject'

urlpatterns = [
     path("", views.empty, name="empty"),
     path('generate/' , views.generate ,name='generate'),
     path('text/' ,views.content , name="textgenerate")
]