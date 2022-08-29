from django.db import models

class bill(models.Model):
    id = models.AutoField(primary_key=True)
    income = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2,
        verbose_name="收入"
    )
    note = models.CharField(
        max_length=128,
        default="",
        verbose_name="备注"
    )
    data_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="bill创建时间"
    )
    billtype = models.ForeignKey(
        'bill_type',
        on_delete=models.PROTECT,
        verbose_name="bill类型"
    )

    class Meta:
        app_label = 'app'

class bill_type(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(
        max_length=16,
        unique=True
    )

    class Meta:
        app_label = 'app'