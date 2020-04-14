from django.db import models

# Create your models here.


class Permission(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    is_menu = models.BooleanField(verbose_name="是否是菜单", default=False)
    html = models.CharField(verbose_name="所属的静态页面", max_length=50)
    menu = models.ForeignKey(verbose_name="所属的菜单", to="Menu", blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(verbose_name="菜单名", max_length=20)

    def __str__(self):
        return self.name
