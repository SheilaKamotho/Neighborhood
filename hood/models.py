# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NeighborHood(models.Model):
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length = 100)
    occupant_count = models.PositiveIntegerField(default=0)
    # admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    

    def save_neighborhood(self):
        self.save()

    @classmethod
    def save_neighborhood(cls):
        hoods=cls.objects.filter()
        return hoods

