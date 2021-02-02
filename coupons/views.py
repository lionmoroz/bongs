from django.shortcuts import render , redirect
from django.utils import timezone
from cart.cart import Cart
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponAplyForm
from decimal import Decimal

# Create your views here.


def coupon_apply(request):
    cart = Cart(request)
    now = timezone.now()
    form = CouponAplyForm(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            coupon.save()    
            request.session['coupon_id'] = coupon.id

            coupon.user.add(request.user)
            coupon.number +=1
			
			
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')