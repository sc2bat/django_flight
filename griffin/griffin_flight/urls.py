from django.urls import path
from . import views

urlpatterns = [

    # 테이블 전체
    path('admins/', views.admin, name='admin'),
    path('books/', views.book),
    path('users/', views.user),
    path('flights/', views.flight),
    path('airplanes/', views.airplane),
    path('airports/', views.airport),
    path('passports/', views.passport),

    path('<int:flight_id>', views.flight_test, name='flight_test'),
]