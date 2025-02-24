from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),   # 🔑 Register Page
    path('login/', views.login_view, name='login'),            # 🔑 Login Page
    path('logout/', views.logout_view, name='logout'),         # 🔑 Logout
    path('', views.home_view, name='home'),                    # 🏠 Home Page
]
