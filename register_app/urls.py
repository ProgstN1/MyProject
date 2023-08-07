from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg_page, name='reg_page'),
]