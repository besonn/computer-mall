from django.db import models
from df_user.models import UserInfo
from df_order.models import OrderInfo
from datetime import datetime
# Create your models here.

class Coupons(models.Model):

    type = models.IntegerField(verbose_name="类型，1为满减",null=True )
    name = models.CharField(default="",max_length=32, verbose_name="优惠券名称", null=True)
    img = models.CharField(default="",max_length=64,verbose_name="图片的url地址", null=True)
    start_time = models.DateTimeField(default="",verbose_name="优惠券起始时间",null=True)
    money = models.DecimalField(default="", max_digits=10,decimal_places=2,verbose_name="金额")
    status = models.IntegerField(default="", verbose_name="0未开始，1进行中，-1是结束")
    remarks = models.CharField(default="",max_length=512, verbose_name="优惠券的说明", null=True)
    create_time = models.DateTimeField(default="",verbose_name="创建时间", null=True)
    full_money = models.DecimalField(default="",verbose_name="金额满", max_digits=10,decimal_places=2,null=True)

    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

    class Meta:
        verbose_name = "优惠券信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name;


class Coupons_recive(models.Model):

    #good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品ID")
    buyer = models.ForeignKey(UserInfo,on_delete=models.CASCADE,verbose_name="用户的id")
    coupon = models.ForeignKey(Coupons,on_delete=models.CASCADE, verbose_name="优惠券的id")
    coupon_money = models.DecimalField(default="", max_digits=10,decimal_places=2,verbose_name="优惠券的金额", null=True)
    status = models.IntegerField(default="", verbose_name="状态，1为已使用，0为已领取未使用，-1为已过期")
    create_time = models.DateTimeField(default="", verbose_name="领取时间", null=True)
    full_money = models.DecimalField(default="", max_digits=10,decimal_places=2,verbose_name="金额满", null=True)

    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

    class Meta:
        verbose_name = "优惠券领取记录表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.buyer_id;


class Coupons_Logs(models.Model):
    # good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品ID")
    buyer = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户的id")
    coupon_recive = models.ForeignKey(Coupons_recive, on_delete=models.CASCADE, verbose_name="领取优惠券的id")
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单的id")
    coupon_money = models.DecimalField(default="", max_digits=10,decimal_places=2,verbose_name="优惠券的金额", null=True)
    order_final_amount = models.DecimalField(default="",max_digits=10,decimal_places=2,verbose_name="订单的最终金额")
    status = models.IntegerField(default="", verbose_name="日志状态: 默认为0，支付回调成功后为1")
    create_time = models.DateTimeField(default="", verbose_name="领取时间", null=True)

    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

    class Meta:
        verbose_name = "优惠券消费记录表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_final_amount;