from django.db import models
from django.shortcuts import reverse


class Tvl(models.Model):
    destination_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    popular_season = models.CharField(max_length=100)


    def get_detail_url(self):
        return reverse('travel:detail', args=[self.pk])


    def get_delete_url(self):
        return reverse('travel:delete', args=[self.pk])


    def get_update_url(self):
        return reverse('travel:update', args=[self.pk])