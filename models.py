from django.db import models


class File(models.Model):
    name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='files/')
    upload_date = models.DateField(auto_now_add=True)