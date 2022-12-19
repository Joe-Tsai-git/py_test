from django.db import models
class Device(models.Model):
    # group_choices = (
    #     ('0', '一组'),
    #     ('1', '二组'),
    #     ('3', '三组'),
    # )
    ip = models.GenericIPAddressField(verbose_name='IP地址',unique=True)
    name = models.CharField(verbose_name='设备名称', null=False, blank=False, max_length=64)
#    sn = models.CharField(verbose_name='序列号', null=False, blank=False, max_length=128, unique=True)
    vendor = models.CharField(verbose_name='厂商', null=False, blank=False, max_length=32)
    platform = models.CharField(verbose_name='平台(netmiko)', null=True, blank=True, max_length=128)
    model = models.CharField(verbose_name='型号', default='', max_length=128)
    series = models.CharField(verbose_name='序列号', null=True, blank=True, max_length=128)
    username = models.CharField(verbose_name='用户名', null=True, blank=True, max_length=128)
    password = models.CharField(verbose_name='密码', null=True, blank=True, max_length=128)
    secret = models.CharField(verbose_name='secret', max_length=128, null=True, blank=True)
    port = models.IntegerField(verbose_name='ssh端口', default=22)
#    is_virtual = models.BooleanField(verbose_name='虚拟化', default=False)
#    group = models.CharField('运维组', choices=group_choices, max_length=32)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self) -> str:
        return '设备： {}, {}'.format(self.ip, self.name)

class Interface(models.Model):
    name = models.CharField(verbose_name='设备名称', null=False, blank=False, max_length=64)
    desc = models.CharField(verbose_name='端口描述', max_length=128)
    device = models.ForeignKey('Device', verbose_name='设备', on_delete=models.CASCADE)

#    class Meta:
        
        #unique_togeter = ('name', 'device')
    def __str__(self) -> str:
        return '{} {}'.format(self.device, self.name)
# Create your models here.
