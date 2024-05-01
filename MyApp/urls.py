from django.urls import path
from . import views

urlpatterns=[
    path('api/',views.api_view.as_view()),
    path('',views.home_view,name='home')
]