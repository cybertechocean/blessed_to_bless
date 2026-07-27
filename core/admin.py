from django.contrib import admin

from .models import (
    Campaign,
    ContactMessage,
    GalleryImage,
    NewsArticle,
    Programme,
    VolunteerApplication,
)


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("title", "ordering", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("ordering", "title")


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("title", "raised", "goal", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("title", "excerpt", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "is_active")
    list_filter = ("category", "featured", "is_active")
    search_fields = ("title", "caption")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "handled", "created_at")
    list_filter = ("handled", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at", "updated_at")


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "area_of_interest", "contacted", "created_at")
    list_filter = ("contacted", "created_at")
    search_fields = ("name", "email", "area_of_interest", "message")
    readonly_fields = ("created_at", "updated_at")