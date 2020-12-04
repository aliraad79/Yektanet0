from django.db import models
from django.shortcuts import reverse


class Advertiser(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show-all-ads')

    def get_clicks(self):
        counter = 0
        for i in self.ads.all():
            counter += i.clicks
        return counter

    def get_views(self):
        counter = 0
        for i in self.ads.all():
            counter += i.views
        return counter


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='ads_pics')
    link = models.URLField(max_length=1000)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return self.title + " " + str(self.id)

    def add_click(self):
        self.clicks += 1
        self.save()

    def add_view(self):
        self.views += 1
        self.save()

    def get_absolute_url(self):
        return reverse('show-all-ads')
