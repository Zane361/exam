from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]