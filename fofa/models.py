from django.db import models
from user.models import User
# Create your models here.


class Admin(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AlbumIndex(models.Model):
    index_name = models.CharField(max_length=20, blank=True, null=True)
    audio_url = models.CharField(max_length=50, blank=True, null=True)
    audio_size = models.CharField(max_length=10, blank=True, null=True)
    album = models.ForeignKey('AlbumList', models.DO_NOTHING, blank=True, null=True)
    audio_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album_index'


class AlbumList(models.Model):
    album_name = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    speaker = models.CharField(max_length=20, blank=True, null=True)
    index_num = models.CharField(max_length=5, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    album_image = models.CharField(max_length=50, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album_list'


class ArticleList(models.Model):
    header = models.CharField(max_length=50, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    dashi = models.ForeignKey('Dashi', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_list'


class CountNum(models.Model):
    count_name = models.CharField(max_length=20, blank=True, null=True)
    read_num = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    homework = models.ForeignKey('Homework', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'count_num'


class Dashi(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashi'


class Homework(models.Model):
    homework_name = models.CharField(max_length=20, blank=True, null=True)
    homework_category = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homework'


