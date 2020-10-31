# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

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

class Profile(models.Model):
    name = models.CharField(max_length = 60)
    id_no = models.IntegerField()
    hood_id = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)
    email = models.CharField(max_length = 60)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    @classmethod
    def save_profile(cls):
        profile=cls.objects.filter()
        return profile

class Business(models.Model):
    name = models.CharField(max_length = 60)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hood_id = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)
    email = models.CharField(max_length = 100)

    def save_business(self):
        self.save()

    @classmethod
    def save_business(cls):
        businesses = cls.objects.filter()
        return businesses



