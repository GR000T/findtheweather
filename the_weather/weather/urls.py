from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogPostSitemap

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<city_name>/',views.delete_city,name='delete_city'),
    path('sitemap.xml', BlogPostSitemap, {'sitemaps': sitemap},name='django.contrib.sitemaps.views.sitemap'),
]
