from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=200)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name

class Produk(models.Model):
    nm_produk = models.CharField(max_length=200)
    harga = models.FloatField()
    berat = models.IntegerField()
    deskripsi = models.TextField()
    merek = models.CharField(max_length=200)
    jenis_produk = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    size = models.IntegerField()
    bahan = models.CharField(max_length=200)
    stok = models.IntegerField()
    gambar = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nm_produk