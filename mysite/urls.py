from django.urls import path

from . import views
app_name = 'mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<nId>', views.detail, name='detail'),
]