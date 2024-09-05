from django.urls import path
from . import views     # from current folder importing views

# url configuration
urlpatterns = [
    path('test/',views.say_hello),
    path('login/',views.login_page),
    path('booking/',views.booking_page),
    path('status/',views.status_page),
    path('slots/',views.slot_page),
    path('info/',views.info_page),
    path('info/<str:ticket_no>/', views.info_page, name='info'),

    path('logout/',views.logout),

    path('checkout/',views.checkout_page),
    path('parking/',views.parking_list_page),
    # path('invoice/',views.invoice_page),
    path('invoice/<str:ticket_no>/', views.invoice_page, name='invoice'),



    path('',views.home_page),



]



