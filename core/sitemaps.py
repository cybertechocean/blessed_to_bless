from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return ["home", "about", "vision-mission", "programmes", "campaign", "donate", "volunteer", "news", "gallery", "contact", "faqs"]

    def location(self, item):
        return reverse(item)