from django.contrib.sitemaps import Sitemap
#from django.shortcuts import reverse
from .models import City

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return City.objects.all()
