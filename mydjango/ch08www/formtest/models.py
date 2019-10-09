from django.db import models

# Create your models here.


class Mood(models.Model):
    status = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.status


class Post(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, verbose_name='选择心情')
    nickname = models.CharField(max_length=20, default='一位不愿透露姓名的勇士', verbose_name='昵称')
    message = models.TextField(null=False, verbose_name='内容/消息')
    del_pass = models.CharField(max_length=10, default=123456,)
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    enabled = models.BooleanField(default=False, verbose_name='是否呈现出来')


    def __str__(self):
        return self.message