from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()


class team(models.Model):
    name_t = models.CharField(max_length=250)
    img_t = models.ImageField(upload_to='pictures')
    desc_t = models.TextField()


def __str__(self):
    return self.name
