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
        self.new_profile=Profile(name = 'Sheila')

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
        self.assertTrue(self.updated_profile.name,'sheila')

    def test_profile_delete(self):
        self.profile.save_profile()
        self.searched_profile = Profile.objects.get(id==1)
        self.searched_profile.delete_profile()
        self.assertTrue(len(Profile.objects.all()) == 0)

