#系统包
from datetime import datetime


#第三方包
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.CharField(max_length=100, null=True, blank=True, verbose_name="出生年月")
    mobile = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")))
    gender = models.CharField(max_length=11, verbose_name="电话")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="电子邮箱")

    class Meta:
        # 设置模型直观可读的名称,复数表示
        verbose_name = "用户"
        # 设置模型直观可读的名称,复数表示
        verbose_name_plural = "用户"

    # 设置模型的返回值
    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code