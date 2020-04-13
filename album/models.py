from django.db import models

# Create your models here.


class AlbumIndex(models.Model):
    index_name = models.CharField(max_length=20, blank=True, null=True)
    audio_url = models.CharField(max_length=50, blank=True, null=True)
    audio_size = models.CharField(max_length=10, blank=True, null=True)
    album = models.ForeignKey('AlbumList', models.DO_NOTHING, blank=True, null=True)
    audio_time = models.CharField(max_length=20, blank=True, null=True)

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
    status = models.CharField(max_length=20, blank=True, null=True)
    album_image = models.CharField(max_length=50, blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album_list'
