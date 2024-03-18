from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'registration/', views.registration, name='registration'),
    re_path(r'user_login/', views.user_login, name='user_login'),
    re_path(r'dash/', views.dash, name='dash'),
    path('book/<str:train_number>/', views.book, name='book'),
    re_path(r'search_train/', views.search_train, name='search_train'),
    path('book_seat/', views.book_seat, name='book_seat'),
    path('get_seats/<str:train_id>/', views.get_seats, name='get_seats'),
    path('confirmation/<int:booking_id>/<str:email>/<str:username>/<str:train_number>/', views.confirm, name='confirmation'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    re_path(r'booking_list/', views.booking_list, name='booking_list'),
    re_path(r'logout_user/', views.logout_user, name='logout_user'),

]