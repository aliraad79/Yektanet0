from django.db import models
from django.shortcuts import reverse
from datetime import datetime


class Click(models.Model):
    advertiser_id = models.IntegerField()
    ad_id = models.IntegerField()
    ip = models.GenericIPAddressField()
    click_time = models.DateTimeField(auto_now_add=True)


class View(models.Model):
    advertiser_id = models.IntegerField()
    ad_id = models.IntegerField()
    ip = models.GenericIPAddressField()
    view_time = models.DateTimeField(auto_now_add=True)


class Advertiser(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show-all-ads')

    def get_clicks(self):
        return Click.objects.filter(advertiser_id=self.id).count()

    def get_views(self):
        return View.objects.filter(advertiser_id=self.id).count()


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='ads_pics')
    link = models.URLField(max_length=1000)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads')
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " " + str(self.id)

    def add_click(self, ip):
        Click.objects.create(advertiser_id=self.advertiser.id, ad_id=self.id, ip=ip, click_time=datetime.now())

    def add_view(self, ip):
        View.objects.create(advertiser_id=self.advertiser.id, ad_id=self.id, ip=ip, click_time=datetime.now())

    def get_absolute_url(self):
        return reverse('show-all-ads')

    def approve_ad(self):
        self.approve = True
