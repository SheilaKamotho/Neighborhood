# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NeighborHood(models.Model):
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length = 100)
    occupant_count = models.PositiveIntegerField(default=0)
    # admin = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def save_neighborhood(self):
        self.save()

    def __str__(self):
        return self.name

    @classmethod
    def save_neighborhood(cls):
        hoods=cls.objects.filter()
        return hoods

    def save_neighborhood(self):
        self.save()
    
    def update_neighborhood(self):
        self.update()

    def delete_neighborhood():
        self.delete()

class Profile(models.Model):
    full_name = models.CharField(max_length = 60, null=True, blank=True)
    id_no = models.IntegerField( null=True, blank=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE,  null=True, blank=True)
    email = models.CharField(max_length = 60, null=True, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


    @classmethod
    def save_profile(cls):
        profile=cls.objects.filter()
        return profile

    def save_profile(self):
        self.save()
    
    def update_profile(self):
        self.update()

    def delete_profile():
        self.delete()

    

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

    def save_business(self):
        self.save()
    
    def update_business(self):
        self.update()

    def delete_business():
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses


class Post(models.Model):
    title = models.CharField(max_length = 60)
    image = models.ImageField(upload_to = 'image/')
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_post(self):
        self.save()

    @classmethod
    def save_post(cls):
        projects=cls.objects.filter()
        return posts
