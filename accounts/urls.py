
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('searchflights',views.searchflights,name='searchflights'),
    path('payment',views.payment,name='payment'),
    path('BookTickets',views.BookTickets,name='BookTickets'),
    path('feedback',views.feedback,name='feedback'),
]
