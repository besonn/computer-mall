from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from df_user import user_decorator
import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from time import gmtime,strftime
import time,datetime
from df_user.models import UserInfo
from df_cart.models import CartInfo
from df_user.models import GoodsBrowser
from df_goods.models import GoodsInfo
from urllib.parse import urlparse
from df_comments.models import CommentInfo
@user_decorator.login
def add(request, gid, com, point = 5): #四个参数,request,商品id,评论内容,评论星级(默认5星)
    uid = request.session['user_id']
    gid, com, point = int(gid), str(com), int(point)
    #新建一条评论
    user = UserInfo.objects.filter(id=uid)[0]
    goods = GoodsInfo.objects.filter(id=gid)[0]
    comments = CommentInfo(user, goods, com, point)
    comments.save()
# Create your views here.


@user_decorator.login
def delete(request, cid):
    comments = CommentInfo.objects.get(id=cid)
    comment = comments[0]
    comment.delete()


def show(request, gid):
    comments_list = CommentInfo.objects.filter(goods=GoodsInfo.objects.filter(id=gid))
    context = {
        'title': '评论列表',
        'comments_list': comments_list,
    }
    return render(request, 'df_goods/detail.html', context)


@user_decorator.login
def modify(request, cid, com, point):
    comments = CommentInfo.objects.filter(id=cid)
    comment = comments[0]
    comment.comment_text = com
    comment.point = point
    comment.create_time = datetime.now()


@user_decorator.login
def push(request):
    goodsdata = {}
    gid = request.POST.get('good_id')
    goodsid = gid
    uid = request.session['user_id']
    user = UserInfo.objects.filter(id=uid)[0]
    goods = GoodsInfo.objects.filter(id=goodsid)[0]
    print(goodsid)
    point = 5
    com = request.POST.get('comment')
    print(com)
    comments = CommentInfo()
    comments.user = user
    comments.goods = goods
    comments.comment_text = com
    comments.point = 5
    ite = request.POST['OffPref']
    comments.point=ite
    comments.create_time=datetime.datetime.now()
    # comments = CommentInfo(uid, gid, com, point)
    comments.save()
    goodsdata['提交成功！']=1
    return HttpResponse(goodsdata)

