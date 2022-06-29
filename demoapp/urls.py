from . import views
from django.urls import path

urlpatterns = [
  path('load_homepage',views.load_homepage,name='load_homepage'),
  path('load_subpage',views.load_subpage,name='load_subpage'),
 
  path('mul_two_nos',views.mul_two_nos,name='mul_two_nos'),
]