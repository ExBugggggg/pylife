from django.db import models

class login(models.Model):
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="用户名称"
    )
    email = models.CharField(
        max_length=254,
        unique=True,
        verbose_name="邮箱"
    )
    ip = models.CharField(
        max_length=15,
        verbose_name="登录ip地址"
    )
    token = models.CharField(
        
    )

    class Meta:
        app_label = 'app'