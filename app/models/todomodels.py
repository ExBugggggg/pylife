from django.db import models

class todo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=32, 
        default="",
        verbose_name="todo名称"
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="todo创建时间"
    )
    note = models.CharField(
        max_length=128,
        default="",
        verbose_name="todo备注"
    )
    finished = models.BooleanField(
        default=False, 
        verbose_name="todo是否完成"
    )
    date_finished = models.DateTimeField(
        auto_now=True,
        verbose_name="todo结束时间"
    )
    typeid = models.SmallIntegerField(
        verbose_name="todo_type的id"
    )

    class Meta:
        app_label = 'app'

class todo_type(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(
        max_length=10, 
        verbose_name="todo类型名称", 
        unique=True
    )
    color = models.CharField(
        max_length=10,
        default="", 
        verbose_name="todo标签的颜色"
    )

    class Meta:
        app_label = 'app'