from django.db import models

class article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        verbose_name="文章名称"
    )
    short_description = models.CharField(
        max_length=512,
        verbose_name="文章简短描述"
    )
    category = models.ForeignKey(
        'categorymodels.category',
        on_delete=models.PROTECT,
        verbose_name="文章类别id"
    )
    # tagid 由tag中的tagid提供
    tagid = models.CharField(
        max_length=100,
        verbose_name="文章标签"
    )
    save_path = models.SlugField(
        max_length=128,
        verbose_name="文章存储路径"
    )
    data_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="article创建时间"
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        verbose_name="article更新时间"
    )