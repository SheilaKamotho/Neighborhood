# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Profile

# Create your tests here.
class ProfileClass(TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_profile=Profile(name = 'bakari')

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_update_method(self):
        self.new_profile.save_profile()
        self.new_profile= Profile.objects.filter(id==1).update()
        self.updated_profile=Profile.objects.get(id==1)
        self.assertTrue(self.updated_profile.name,'bakari')

    def test_profile_delete(self):
        self.profile.save_profile()
        self.searched_profile = Profile.objects.get(id==1)
        self.searched_profile.delete_profile()
        self.assertTrue(len(Profile.objects.all()) == 0)

class BusinesClass(TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_business(name = 'Bakes')

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_business,Business))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses)>0)

    def test_update_method(self):
        self.new_business.save_business()
        self.new_business= Business.objects.filter(id==1).update()
        self.updated_business=Business.objects.get(id==1)
        self.assertTrue(self.updated_business.name,'Bakes')

    def test_business_delete(self):
        self.business.save_business()
        self.searched_business = Business.objects.get(id==1)
        self.searched_business.delete_business()
        self.assertTrue(len(Business.objects.all()) == 0)

class NeighborHoodClass(TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_neighborhood=Neighborhood(name = 'Kidfarmaco')

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_neighborhood.save_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoodS)>0)

    def test_update_method(self):
        self.new_neighborhood.save_neighborhood()
        self.new_neighborhood= Neighborhood.objects.filter(id==1).update()
        self.updated_neighborhood=Neighborhood.objects.get(id==1)
        self.assertTrue(self.updated_neighborhood.name,'Kidfarmaco')

    def test_neighborhood_delete(self):
        self.neighborhood.save_neighborhood()
        self.searched_neighborhood = Neighborhood.objects.get(id==1)
        self.searched_neighborhood.delete_neighborhood()
        self.assertTrue(len(Neighborhood.objects.all()) == 0)

