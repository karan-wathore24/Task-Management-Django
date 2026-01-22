from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('register/', views.register, name="register"),
    path('login_page/', views.login_page, name="login_page"),
    path('loginsave/', views.loginsave, name='loginsave'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('user_logout/', views.user_logout, name="logout"),
    path('reset_ps/', views.reset_ps, name="reset_ps"),
    path('set_ps/', views.set_ps, name="set_ps"),
    path('forget_ps/',views.forget_ps,name="forget_ps"),
    path('forget_valid/', views.forget_valid, name="forget_valid"),
    path('upd_pss/', views.upd_pss, name="upd_pss"),
    path('upd_pss/',views.upd_pss,name="upd_pss"),
]
