from django.urls import path
from . import views
#from pyshop.urls import urlpatterns


urlpatterns=[
    path('',views.index),
]