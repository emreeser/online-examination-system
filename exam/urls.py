from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('exam/<int:eid>/', views.quiz_view, name='exam'),
    path('forgot/', views.forgot_view, name='forgot'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('reset/<int:uid>/', views.reset_view, name='reset'),
    path('finish/', views.finish_view, name='finish'),
]