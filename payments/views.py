from typing_extensions import Required
from django.shortcuts import render


@login_required
def BasketView ( request ) :
    return render ( request , ' payment/home.html')