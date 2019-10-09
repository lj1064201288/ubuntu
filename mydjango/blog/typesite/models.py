from django.db import models
from time import timezone

# Create your models here.
class User(models.Model):

    SEX = [
        (1, '男'),
        (2, "女"),
    ]

    user_full_name = models.CharField('用户名', max_length=30, null=True, blank=True, )
    user_name = models.CharField('账号', max_length=30)
    user_password = models.CharField('密码', max_length=30)
    user_email = models.CharField('邮箱', max_length=45, null=True, blank=True)
    user_sex = models.IntegerField('性别', choices=SEX, default=1)
    user_age = models.IntegerField('年龄')
    user_phone_number = models.CharField('电话号码', null=True, blank=True, max_length=20,)
    user_card = models.CharField('身份证号码', max_length=30)
    createby = models.CharField('创建者', max_length=32)
    createtime = models.DateTimeField('创建时间', auto_now_add=True)
    updateby = models.CharField('更新者', max_length=32, null=True)
    updatetime = models.DateTimeField('更新时间', blank=True, null=True)
    is_active = models.IntegerField('是否使用', blank=True, null=True, default=1)
    img_url = models.ImageField('头像', upload_to='img', blank=True, null=True)

    class Meta:
        db_table = 'sys_user'

class Blog(models.Model):
    pass
class Comment(models.Model):
    pass