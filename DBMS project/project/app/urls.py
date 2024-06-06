
from django.urls import path
from app import views
from app.views import sell_car

urlpatterns = [
    path('', views.index,name='index'),
    path('login', views.handlelogin,name='handlelogin'),
    path('signup', views.handlesignup,name='handlesignup'),
    path('sell', views.sell,name='sell'),
    path('buy/', views.buy_car, name='buy_car'),
    path('sell/', views.sell_car, name='sell_car'),
    
]
