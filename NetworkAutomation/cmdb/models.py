from django.db import models
class Device(models.Model):
    group_choices = (
        ('0', '一组'),
        ('1', '二组'),
        ('3', '三组'),
    )
    ip = models.GenericIPAddressField(verbose_name='IP地址')
    name = models.CharField(verbose_name='设备名称', null=False, blank=False, max_length=64)
    sn = models.CharField(verbose_name='序列号', null=False, blank=False, max_length=128, unique=True)
    vendor = models.CharField(verbose_name='厂商', null=False, blank=False, max_length=32)
    is_virtual = models.BooleanField(verbose_name='虚拟化', default=False)
    group = models.CharField('运维组', choices=group_choices, max_length=32)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self) -> str:
        return '设备： {}, {}'.format(self.name, self.ip)

    
# Create your models here.
