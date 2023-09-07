

from django.urls import path
from .import views
app_name = 'gaming'

urlpatterns = [
    path("", views.index, name="index" ),
    path("<int:product_id>", views.details, name="details"),
    path("checkout/", views.checkout, name="checkout" )
  
   
]
