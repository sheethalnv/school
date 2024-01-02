from . import views
from django.urls import path, include
app_name='school'
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('utility/',views.utility,name='utility'),
    path('details/',views.details,name='details'),
    path('load_cources',views.load_cources,name='load_cources'),
]