from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^post/$',views.new_post,name = 'post'),
    url(r'^business/$',views.business,name = 'business'),
    url(r'^contact/$',views.contact,name = 'contact'),
    url(r'^about/$',views.about,name = 'about'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^user/profile/', views.profile, name='profile'),
    url(r'^update/user/',views.update_profile, name='edit_profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)