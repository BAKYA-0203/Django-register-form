from . import views
from django.urls import path
urlpatterns = [
   
   #path('admin',views.index,name="index"),
   path('',views.home,name="home"),
   path('register/',views.register,name="register"),
   path('view/',views.view,name="view"),
   path('update/<int:id>',views.update),
   path('upemp/<int:id>',views.upemp),
   path('delemp/<int:id>',views.delemp),
]