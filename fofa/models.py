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


class CountNum(models.Model):
    count_name = models.CharField(max_length=20, blank=True, null=True)
    read_num = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    homework = models.ForeignKey('Homework', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'count_num'


class Homework(models.Model):
    homework_name = models.CharField(max_length=20, blank=True, null=True)
    homework_category = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homework'


