from django.db import models

# Create your models here.

class Advertiser(models.Model):
    id = models.IntegerField(primary_key=True ,unique=True)
    name = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ad(models.Model):
    id = models.IntegerField(primary_key=True ,unique=True)
    title = models.CharField(max_length=500)
    imgUrl = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey(Advertiser,on_delete=models.CASCADE)

    def __str__(self):
        return self.title+ " " + str(self.id)
