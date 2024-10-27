from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('thank-you', views.thankpage, name='thankpage')
]