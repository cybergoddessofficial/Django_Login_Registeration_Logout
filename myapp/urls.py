from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Index,name="Index"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('userindex',views.userindex,name="userindex"),
    path('logout',views.logout,name="logout")
]
