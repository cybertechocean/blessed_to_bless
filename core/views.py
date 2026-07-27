from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, VolunteerForm
from .models import Campaign, GalleryImage, NewsArticle, Programme

PROGRAMMES = [
    ("Emergency Relief", "Rapid, dignified support for families facing crisis.", "We provide essentials and protection to people affected by conflict, displacement and disaster.", "heart-handshake", "emergency-relief"),
    ("WASH", "Safe water, sanitation and hygiene for healthier communities.", "From boreholes to hygiene education, we help communities build lasting foundations for health.", "droplets", "wash"),
    ("Healthcare", "Bringing compassionate healthcare closer to people.", "We partner with local health workers to improve access to primary care, maternal health and referrals.", "stethoscope", "healthcare"),
    ("Education", "Opening doors through safe, inclusive learning.", "We support children and young people with learning spaces, materials and the confidence to thrive.", "graduation-cap", "education"),
    ("Women Empowerment", "Investing in the leadership and livelihoods of women.", "Skills, savings groups and protection programmes help women build secure futures for their families.", "users", "women-empowerment"),
    ("Youth Development", "Equipping the next generation to lead.", "We create pathways for young people through life skills, mentorship, training and civic participation.", "sparkles", "youth-development"),
    ("Child Care & Protection", "Every child deserves safety, dignity and a future.", "We work with families and communities to keep children safe and help them recover and belong.", "baby", "child-care-protection"),
    ("Elderly Support", "Honouring older people with care and connection.", "We provide practical support and meaningful community connection for older people living in vulnerability.", "hand-heart", "elderly-support"),
    ("Disability Inclusion", "Removing barriers so everyone can participate.", "We promote accessibility, inclusive services and opportunity for people with disabilities.", "accessibility", "disability-inclusion"),
    ("Livelihood Improvement", "Building resilient livelihoods that last.", "Training, tools and market connections help families move from surviving to planning for tomorrow.", "sprout", "livelihood-improvement"),
    ("Disaster Response", "Prepared communities respond more safely.", "We help communities prepare for hazards, respond quickly and recover with resilience.", "shield-plus", "disaster-response"),
    ("Community Development", "Local leadership for lasting change.", "Together with communities, we design solutions that reflect local knowledge, priorities and hope.", "landmark", "community-development"),
]

PROGRAMME_IMAGES = {
    "emergency-relief": "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&w=1200&q=80",
    "wash": "https://images.unsplash.com/photo-1541544741938-0af808871cc0?auto=format&fit=crop&w=1200&q=80",
    "healthcare": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?auto=format&fit=crop&w=1200&q=80",
    "education": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1200&q=80",
    "women-empowerment": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=1200&q=80",
    "youth-development": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1200&q=80",
}

DEFAULT_NEWS = [
    {"title": "Standing with families in East DR Congo", "category": "Emergency appeal", "date": "May 28, 2026", "excerpt": "Our teams and community partners are responding with dignity, practical support and hope.", "image": "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&w=900&q=80"},
    {"title": "A safe place to learn, a reason to dream", "category": "Success story", "date": "April 16, 2026", "excerpt": "Meet the community educators creating brighter futures for children in Kinshasa.", "image": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=900&q=80"},
    {"title": "Growing stronger together in Kenya", "category": "Project update", "date": "March 09, 2026", "excerpt": "Local leadership is at the heart of our new livelihoods and resilience programme.", "image": "https://images.unsplash.com/photo-1532629345422-7515f3d16bb6?auto=format&fit=crop&w=900&q=80"},
]

DEFAULT_GALLERY = [
    ("A community built on care", "Community", "https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?auto=format&fit=crop&w=900&q=80"),
    ("Learning without limits", "Education", "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=900&q=80"),
    ("Together, we move forward", "Community", "https://images.unsplash.com/photo-1559027615-cd4628902d4a?auto=format&fit=crop&w=900&q=80"),
    ("A healthier tomorrow", "Healthcare", "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=900&q=80"),
    ("Hope has many hands", "Livelihoods", "https://images.unsplash.com/photo-1542810634-71277d95dcbb?auto=format&fit=crop&w=900&q=80"),
    ("Women leading change", "Empowerment", "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?auto=format&fit=crop&w=900&q=80"),
]


def _programmes():
    saved = list(Programme.objects.filter(is_active=True))
    if saved:
        return saved
    return [
        {"title": title, "summary": summary, "description": description, "icon": icon, "slug": slug, "image_url": PROGRAMME_IMAGES.get(slug, PROGRAMME_IMAGES["education"])}
        for title, summary, description, icon, slug in PROGRAMMES
    ]


def _news():
    saved = list(NewsArticle.objects.filter(is_active=True))
    return saved or DEFAULT_NEWS


def _gallery():
    saved = list(GalleryImage.objects.filter(is_active=True))
    return saved or [{"title": title, "category": category, "image_url": image} for title, category, image in DEFAULT_GALLERY]


def home(request):
    programmes = _programmes()
    return render(request, "core/home.html", {"programmes": programmes, "featured_programmes": programmes[:6], "news": _news()[:3]})


def about(request):
    return render(request, "core/about.html")


def programmes(request):
    return render(request, "core/programmes.html", {"programmes": _programmes()})


def programme_detail(request, slug):
    programme = next((item for item in _programmes() if item["slug"] == slug) if isinstance(_programmes()[0], dict) else (item for item in _programmes() if item.slug == slug), None)
    if not programme:
        programme = get_object_or_404(Programme, slug=slug, is_active=True)
    return render(request, "core/programme_detail.html", {"programme": programme})


def campaign(request):
    saved = Campaign.objects.filter(is_active=True).first()
    data = saved or {
        "title": "East DR Congo Crisis",
        "summary": "Families in eastern Democratic Republic of Congo need safety, shelter and a path to rebuild.",
        "description": "For communities facing displacement and uncertainty, timely humanitarian support can mean clean water, a safe place to sleep, essential healthcare and the dignity of choosing what comes next.",
        "image_url": "https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?auto=format&fit=crop&w=1600&q=85",
        "goal": 100000,
        "raised": 63400,
        "needs": "Emergency shelter, clean water, healthcare, protection and family essentials.",
        "progress_update": "Community partners are currently prioritising displaced families, children and households led by women.",
    }
    return render(request, "core/campaign.html", {"campaign": data})


def donate(request):
    return render(request, "core/donate.html")


def volunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you. Your volunteer application has been received.")
            return redirect("volunteer")
    else:
        form = VolunteerForm()
    return render(request, "core/volunteer.html", {"form": form})


def news(request):
    page = Paginator(_news(), 6).get_page(request.GET.get("page"))
    return render(request, "core/news.html", {"news": page})


def article_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug, is_active=True)
    return render(request, "core/article_detail.html", {"article": article})


def gallery(request):
    return render(request, "core/gallery.html", {"gallery": _gallery()})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out. We will be in touch soon.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})


def faqs(request):
    return render(request, "core/faqs.html")


def simple_page(request, page):
    return render(request, f"core/{page}.html")