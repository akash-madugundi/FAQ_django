from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('api/faqs/', views.get_faqs, name = 'get_faqs'),
    path('api/faqs/create/', views.create_faq, name='create_faq')
]