from django.db import models

# Create your models here.


class AutoImage(models.Model):
    image = models.CharField(max_length=50, blank=True, null=True)
    image_decoration = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_image'
