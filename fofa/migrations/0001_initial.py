# Generated by Django 2.0.6 on 2020-04-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlbumIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_name', models.CharField(blank=True, max_length=20, null=True)),
                ('audio_url', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_size', models.CharField(blank=True, max_length=10, null=True)),
                ('audio_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'album_index',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlbumList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(blank=True, max_length=20, null=True)),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('speaker', models.CharField(blank=True, max_length=20, null=True)),
                ('index_num', models.CharField(blank=True, max_length=5, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('publish_time', models.DateTimeField(blank=True, null=True)),
                ('album_image', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'album_list',
                'managed': False,
            },
        ),
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
            name='CountNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_name', models.CharField(blank=True, max_length=20, null=True)),
                ('read_num', models.CharField(blank=True, max_length=20, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'count_num',
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
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_name', models.CharField(blank=True, max_length=20, null=True)),
                ('homework_category', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'homework',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('fa_name', models.CharField(blank=True, max_length=20, null=True)),
                ('passeord', models.CharField(blank=True, max_length=20, null=True)),
                ('salt', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=5, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=30, null=True)),
                ('personal_brief', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
