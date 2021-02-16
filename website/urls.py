from django.urls import path
from . import views
urlpatterns = [
   path('', views.home, name ="home"),
   path('home', views.home, name ="home"),
   path('celebritygrid01', views.celebritygrid01, name ="celebritygrid01"),
   path('celebritygrid02', views.celebritygrid02, name ="celebritygrid02"),
   path('celebritylist', views.celebritylist, name ="celebritylist"),
   path('celebritysingle', views.celebritysingle, name ="celebritysingle"),
   path('404Error', views.error, name ="error"),
]