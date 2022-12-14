# Generated by Django 4.1.4 on 2022-12-19 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='IP地址')),
                ('name', models.CharField(max_length=64, verbose_name='设备名称')),
                ('vendor', models.CharField(max_length=32, verbose_name='厂商')),
                ('platform', models.CharField(blank=True, max_length=128, null=True, verbose_name='平台(netmiko)')),
                ('model', models.CharField(default='', max_length=128, verbose_name='型号')),
                ('series', models.CharField(blank=True, max_length=128, null=True, verbose_name='序列号')),
                ('username', models.CharField(blank=True, max_length=128, null=True, verbose_name='用户名')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='密码')),
                ('secret', models.CharField(blank=True, max_length=128, null=True, verbose_name='secret')),
                ('port', models.IntegerField(default=22, verbose_name='ssh端口')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='设备名称')),
                ('desc', models.CharField(max_length=128, verbose_name='端口描述')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.device', verbose_name='设备')),
            ],
        ),
    ]
