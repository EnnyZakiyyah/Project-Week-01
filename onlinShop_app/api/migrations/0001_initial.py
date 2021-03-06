# Generated by Django 3.2.7 on 2021-09-24 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_produk', models.CharField(max_length=200)),
                ('harga', models.FloatField()),
                ('berat', models.IntegerField()),
                ('deskripsi', models.TextField()),
                ('merek', models.CharField(max_length=200)),
                ('jenis_produk', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('size', models.IntegerField()),
                ('bahan', models.CharField(max_length=200)),
                ('stok', models.IntegerField()),
                ('gambar', models.ImageField(upload_to='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
    ]
