# Generated by Django 2.0.6 on 2020-04-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=50, null=True)),
                ('publish_time', models.DateTimeField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'article_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dashi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dashi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='article_pic')),
            ],
            options={
                'db_table': 'content_image',
            },
        ),
    ]
