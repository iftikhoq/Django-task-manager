from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name="home"),
    path('addtask/', views.Addtask, name="addtask"),
    path('edittask/', views.Edittask, name="edittask"),
    path('deletetask/', views.Deletetask, name="deletetask"),
    path('completetask/', views.Completetask, name="completetask"),
    path('addcategory/', views.Addcategory, name="addcategory"),
    path('admin/', admin.site.urls),
]
