import uuid

from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ("ordering", "-created_at")


class Programme(TimestampedModel):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    summary = models.TextField()
    description = models.TextField()
    objectives = models.TextField(blank=True)
    activities = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    icon = models.CharField(max_length=30, default="heart-handshake")

    class Meta(TimestampedModel.Meta):
        verbose_name = "programme"
        verbose_name_plural = "programmes"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("programme-detail", kwargs={"slug": self.slug})


class Campaign(TimestampedModel):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=160)
    summary = models.TextField()
    description = models.TextField()
    image_url = models.URLField(blank=True)
    goal = models.PositiveIntegerField(default=100000)
    raised = models.PositiveIntegerField(default=0)
    needs = models.TextField(blank=True)
    progress_update = models.TextField(blank=True)

    def __str__(self):
        return self.title


class NewsArticle(TimestampedModel):
    CATEGORY_CHOICES = [
        ("story", "Success story"),
        ("update", "Project update"),
        ("appeal", "Emergency appeal"),
        ("news", "Announcement"),
    ]
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=180)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="news")
    excerpt = models.TextField()
    body = models.TextField()
    image_url = models.URLField(blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class GalleryImage(TimestampedModel):
    title = models.CharField(max_length=120)
    caption = models.TextField(blank=True)
    category = models.CharField(max_length=80, default="Community")
    image_url = models.URLField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ContactMessage(TimestampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=160)
    message = models.TextField()
    handled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.subject}"


class VolunteerApplication(TimestampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    area_of_interest = models.CharField(max_length=160)
    message = models.TextField()
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.name