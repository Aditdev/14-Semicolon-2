from django.urls import path
from .migrations import views
app_name = 'payment'

urlpatterns = [
    path ( ' ' , views.BasketView , name = 'basket'),
    ]