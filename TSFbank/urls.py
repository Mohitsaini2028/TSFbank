
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('addcustomer/', views.addcustomer),
    path('cusdetl/', views.cusdetl),
    path('transaction/', views.transaction),
    path('transaction/<str:pk>/', views.send),
    path('send/', views.send),
    path('transactionH/', views.transactionH),
    # path('delete/', views.delete)
]
