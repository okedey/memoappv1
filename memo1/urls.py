from django.urls import path
from . import views

urlpatterns = [
    path('web_home', views.web_home, name='web_home'),
    path('web_create',views.web_create, name='web_create'),
    path('web_delete',views.web_delete, name='web_delete'),
    path('web_detail',views.web_detail, name='web_detail'),
    path('web_edit/<int:num>',views.web_edit, name='web_edit'), 
    path('web_search',views.web_search,name='web_search')
]