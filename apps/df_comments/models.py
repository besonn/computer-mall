from django.db import models

from df_user.models import UserInfo
from df_goods.models import GoodsInfo

import datetime


class CommentInfo(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品")
    comment_text = models.CharField(max_length=512, verbose_name="评论内容")
    point = models.IntegerField(default=5, verbose_name="评分")
    create_time = models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, 0), verbose_name="评论时间")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.uname + '对' + self.goods.gtitle + '的评论'

# Create your models here.
