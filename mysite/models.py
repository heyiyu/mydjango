from django.db import models
from tinymce.models import HTMLField


class Note(models.Model):
    Categorys = (
        ('l', '生活'),
        ('t', '技术'),
        ('e', '经济'),
    )
    nId = models.CharField(verbose_name='id',max_length=100,primary_key=True)
    nPicUrl= models.CharField(verbose_name='图片', max_length=100,null=True,blank=True)
    nTitle = models.CharField(verbose_name='标题',max_length=100)
    nSummary = models.CharField(verbose_name='摘要', max_length=100,null=True,blank=True)
    nContent = HTMLField('正文')
    nCategory = models.CharField(verbose_name='分类', max_length=1, choices=Categorys)
    nTag = models.TextField(verbose_name='标签',max_length=50,null=True,blank=True)
    nCreateTime = models.DateTimeField(verbose_name='创建时间')
    nUpdateTime = models.DateTimeField(verbose_name='更新时间')
    nView = models.IntegerField(verbose_name='阅读量',default=0)
    nLike = models.IntegerField(verbose_name='点赞量',default=0)
    nIsDeleted = models.BooleanField(verbose_name='已删除',default=False)
    nIsPublic = models.BooleanField(verbose_name='公开可见',default=False)
