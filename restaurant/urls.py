from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    # path('menu/', views.menu, name="menu"),
    path('menu/', views.MenuItemsView.as_view(), name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('bookings', views.bookings, name='bookings'), 
    path('bookings', views.BookingView.as_view(), name='bookings'), 
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]