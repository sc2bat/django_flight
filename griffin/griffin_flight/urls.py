from django.urls import path
from . import views

urlpatterns = [

    path('admins/', views.admin, name='admin'),
    path('passports/', views.passport),
    path('flights/', views.flight, name='flight'),
    path('books/', views.book, name='book'),
    path('books/update/', views.updateBook),
    path('airports/', views.airport, name='airport'),
    path('users/', views.user),
    path('airplanes/', views.airplane),
    path('admins_test/', views.admin_test),

    path('payment/', views.payment_join),
    path('flights/search', views.get_flights)
]