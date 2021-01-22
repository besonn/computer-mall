from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from df_coupon.models import Coupons_recive
from df_coupon.models import Coupons_Logs
from df_user import user_decorator
from df_user.models import UserInfo
from df_cart.models import CartInfo
from df_user.models import GoodsBrowser
from df_goods.models import GoodsInfo
from django.contrib.auth.decorators import login_required

@user_decorator.login
def index(request):
    uid = request.session['user_id']
    user = UserInfo.objects.get(id=uid)
    carts = []
   # coupontimes = user.ucoupontimes
    context = {
        'title': '抽奖',
        'page_name': 31,
        'user': user
        # 'value':value
    }
    return render(request, 'df_coupon/index.html', context)
@user_decorator.login
def scene(request):
    uid = request.session['user_id']
    print(uid)
    users = UserInfo.objects.get(id=uid)
    print(users.ucoupontimes)
    coupons = request.POST.get('coupons')
    users.ucoupontimes = max(users.ucoupontimes-1,0)
    users.save()
    couponsInfo =Coupons_recive()
    print(coupons)
    coupons = int(coupons)
    if coupons!=0:
        couponsInfo.buyer_id=uid
        couponsInfo.create_time=datetime.now()
        couponsInfo.status=0
    if coupons == 1:
        couponsInfo.coupon_id=1
        couponsInfo.coupon_money=50.0
        couponsInfo.full_money=0.0
    elif coupons == 2:
        couponsInfo.coupon_id = 2
        couponsInfo.coupon_money = 100.0
        couponsInfo.full_money = 0.0
    elif coupons ==3:
        couponsInfo.coupon_id = 3
        couponsInfo.coupon_money = 500.0
        couponsInfo.full_money = 2500.0
    elif coupons ==4:
        couponsInfo.coupon_id = 4
        couponsInfo.coupon_money = 1000.0
        couponsInfo.full_money = 3000.0

    print(couponsInfo.coupon_money)
    couponsInfo.save()
    context = {
        'title': '信息',
        'coupons': couponsInfo,
        'user': users
    }
    return render(request, 'df_coupon/index.html', context)
