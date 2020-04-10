from django.db import models

# Create your models here.


class ArticleList(models.Model):
    header = models.CharField(max_length=50, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    dashi = models.ForeignKey('Dashi', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_list'


class Dashi(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashi'


class ContentImage(models.Model):
    pic = models.ImageField(upload_to='article_pic', blank=True, null=True)

    class Meta:
        db_table = 'content_image'
