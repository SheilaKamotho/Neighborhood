# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import NeighborHood, Profile, Business, Post

# Register your models here.
admin.site.register(NeighborHood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)