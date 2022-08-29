from django.db import models

class tag(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name="名称"
    )
    description = models.CharField(
        max_length=128,
        default="",
        verbose_name="描述"
    )
    # tagid随机生成
    tagid = models.CharField(
        max_length=5,
        unique=True,
        verbose_name="标签id"
    )
    data_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="tag创建时间"
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        verbose_name="tag更新时间"
    )

    class Meta:
        app_label = 'app'