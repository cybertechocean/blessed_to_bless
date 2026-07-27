from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("vision-mission/", lambda request: views.simple_page(request, "vision_mission"), name="vision-mission"),
    path("programmes/", views.programmes, name="programmes"),
    path("programmes/<slug:slug>/", views.programme_detail, name="programme-detail"),
    path("kenya-project/", lambda request: views.simple_page(request, "kenya_project"), name="kenya-project"),
    path("east-dr-congo-emergency/", views.campaign, name="campaign"),
    path("donate/", views.donate, name="donate"),
    path("volunteer/", views.volunteer, name="volunteer"),
    path("news/", views.news, name="news"),
    path("news/<slug:slug>/", views.article_detail, name="article-detail"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
    path("faqs/", views.faqs, name="faqs"),
    path("privacy-policy/", lambda request: views.simple_page(request, "privacy"), name="privacy"),
    path("terms/", lambda request: views.simple_page(request, "terms"), name="terms"),
]