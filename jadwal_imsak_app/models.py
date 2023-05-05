from django.db import models

# Create your models here.

class Jadwal(models.Model):
    tanggal = models.CharField(max_length=50, null = True, blank = True)
    imsak   = models.TimeField(null=True, blank = True)
    subuh   = models.TimeField(null=True, blank=True)
    terbit  = models.TimeField(null=True, blank=True)
    duha    = models.TimeField(null=True, blank=True)
    zuhur   = models.TimeField(null=True, blank=True)
    asar    = models.TimeField(null=True, blank=True)
    magrib  = models.TimeField(null=True, blank=True)
    iysa    = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'jadwal'

    def __str__(self):
        return self.tanggal

