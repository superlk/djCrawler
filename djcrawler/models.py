from django.db import models


# Create your models here.

class DjData(models.Model):
    name = models.CharField(max_length=255, verbose_name='商品名称')
    price = models.CharField(max_length=255, verbose_name='商品价钱')
    count = models.IntegerField(verbose_name='更新次数')
    update_time = models.DateTimeField(auto_now_add=True, null=True,
                                       blank=True, verbose_name="更新时间")
    url = models.CharField(max_length=255, verbose_name="商品url")
    note = models.CharField(max_length=255, verbose_name="备注")

    class Meta:
        verbose_name = "DJ商品数据"
        verbose_name_plural = "DJ商品数据"
        db_table = 'djdata'

    def __str__(self):
        return self.name, self.price
