from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=20, blank=True, null=True)
    fa_name = models.CharField(max_length=20, blank=True, null=True)
    passeord = models.CharField(max_length=50, blank=True, null=True)
    salt = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    e_mail = models.CharField(max_length=30, blank=True, null=True)
    personal_brief = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='pic', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
