# AI Website Development Prompt — Blessed To Bless Humanity Aid (BBHA)

## ROLE

You are a **Senior Full-Stack Django Developer**, **UI/UX Designer**, **Solution Architect**, **SEO Expert**, and **Humanitarian NGO Website Specialist**.

Your task is to build a **production-ready**, **modern**, **responsive**, **high-performance**, **SEO-optimized**, **secure**, and **scalable** website for **"BLESSED TO BLESS"**.

The website should inspire **trust**, **compassion**, **transparency**, and **hope**, encouraging visitors to support humanitarian causes through donations, volunteering, and partnerships.

The entire project must follow modern Django best practices, reusable architecture, clean code, and scalable design.

---

# PROJECT INFORMATION

## Organization Name

**Blessed To Bless Humanity Aid (BBHA)**

---

## Domain

**https://blessedtobless.org**

---

## Organization Type

International Humanitarian Non-Profit Organization (NGO)

---

## Headquarters

Democratic Republic of Congo (DRC) - Numéro 49, Av Inongo, Quartier Mikonga 2, Kinshasa, DR-CONGO.

Operations also in:

- Kenya
- Tanzania

---

# BRAND IDENTITY

## Motto

> **Changing Lives. Restoring Hope. Empowering Communities.**

---

## Philosophy

> We are blessed to bless others, supported to support others, and helped to help others.

---

## Vision

To be a leading humanitarian organization transforming lives and empowering communities through compassion, dignity, and sustainable development.

---

## Mission

To improve the lives of vulnerable people through humanitarian relief, education, healthcare, empowerment, and sustainable development.

---

# BRAND COLOURS

Primary Blue

```
#00508E
```

Accent Green

```
#1E8F7A
```

White

```
#FFFFFF
```

Dark Text

```
#1F2937
```

Light Background

```
#F5F9FC
```

---

# DESIGN DIRECTION

The design should be inspired by world-class humanitarian organizations such as:

- IFRC (International Federation of Red Cross)
- UNICEF
- UNHCR
- World Vision
- Save the Children

The website should feel:

- Professional
- Clean
- Trustworthy
- Modern
- Inspiring
- Accessible
- Mobile-first

Avoid:

- Generic templates
- Cheap-looking themes
- Excessive animations
- Cluttered layouts

---

# TYPOGRAPHY

Headings

- Poppins

Body

- Inter

Icons

- Lucide Icons

---

# TARGET AUDIENCE

- Individual donors
- Volunteers
- NGOs
- Corporate partners
- Government organizations
- Faith-based organizations
- Community members
- International supporters

---

# PRIMARY GOALS

The website should encourage visitors to:

- Donate
- Volunteer
- Partner
- Learn about BBHA
- Follow humanitarian projects
- Read success stories
- Contact the organization

---

# WEBSITE PAGES

Create the following pages:

- Home
- About Us
- Vision & Mission
- Our Programmes
- Kenya Project
- East DR Congo Emergency
- Donate
- Volunteer
- News & Updates
- Gallery
- Contact
- FAQs
- Privacy Policy
- Terms & Conditions

---

# PROGRAMMES

Support the following programmes:

- Emergency Relief
- WASH
- Healthcare
- Education
- Women Empowerment
- Youth Development
- Child Care & Protection
- Elderly Support
- Disability Inclusion
- Livelihood Improvement
- Disaster Response
- Community Development

Each programme should have:

- Hero image
- Description
- Objectives
- Activities
- Gallery
- Donate button

---

# SPECIAL CAMPAIGN

Create a featured emergency campaign for:

## East DR Congo Crisis

Include:

- Crisis overview
- Images
- Humanitarian needs
- Emergency appeal
- Donate section
- Progress updates

This campaign should be highlighted across the website.

---

# DONATIONS

Create a professional donation page.

Support:

- Bank Account
- Mobile Money

Use placeholders until the client provides account details.

Include:

- Why donate
- Donation impact
- Transparency message
- Frequently Asked Questions

---

# GALLERY

Support:

- Albums
- Categories
- Images
- Captions
- Featured photos

Everything should be editable via Django Admin.

---

# NEWS

Create a news system supporting:

- Articles
- Success stories
- Project updates
- Emergency appeals
- Announcements

Rich content should use:

```
django-ckeditor-5
```

---

# CONTACT

Include:

Founder

Denis Legress Shindani

Phone Numbers

- +243 818 444 877
- +254 729 804 773
- +255 685 437 158

Emails

- info@blessedtobless.org
- blessedtobless@gmail.com

Include:

- Contact form
- Google Maps placeholder
- WhatsApp button
- Social media links

---

# MULTILINGUAL

The website must support:

- English
- French

Use Django Internationalization (i18n).

Do not use automatic translation services.

---

# DJANGO APPLICATIONS

Create modular Django apps:

```
core
```

General website configuration.

```
accounts
```

Future authentication.

```
pages
```

Static pages.

```
programs
```

Humanitarian programmes.

```
campaigns
```

Emergency campaigns.

```
donations
```

Donation management.

```
gallery
```

Images and albums.

```
news
```

News and stories.

```
contact
```

Contact forms.

```
settings
```

Global website settings.

---

# DJANGO ADMIN

Use:

- Django Unfold

The admin interface should be:

- Beautiful
- Organized
- Searchable
- User-friendly

Configure:

- fieldsets
- search_fields
- list_display
- list_filter
- image previews
- ordering
- autocomplete_fields

---

# CONTENT MANAGEMENT

Everything should be editable through Django Admin including:

- Homepage
- Hero banners
- Programme descriptions
- Images
- Gallery
- Contact information
- Social links
- Donation details
- Footer
- SEO settings

Avoid hardcoding content.

---

# DATABASE

Use:

- UUID primary keys
- Slugs
- created_at
- updated_at
- is_active
- ordering

Use proper relationships:

- ForeignKey
- ManyToMany
- OneToOne

---

# SEO

Every page should support:

- Meta title
- Meta description
- Canonical URL
- Open Graph
- Twitter Cards
- Structured Data
- XML Sitemap
- Robots.txt

SEO fields should be editable from Django Admin.

---

# PERFORMANCE

Optimize for:

- Fast loading
- Lazy loading
- WebP images
- Image compression
- Responsive images
- Caching
- Minified assets

Aim for excellent Lighthouse scores.

---

# ACCESSIBILITY

Meet WCAG AA standards.

Support:

- Keyboard navigation
- Proper contrast
- Alt text
- Semantic HTML
- Screen readers

---

# SECURITY

Implement:

- CSRF Protection
- Secure headers
- XSS protection
- SQL Injection protection
- Secure media uploads
- Environment variables for secrets

---

# CODING STANDARDS

Use:

- Django 6.0.7
- Python 3.13+
- PostgreSQL
- Tailwind CSS v4
- HTMX
- Alpine.js
- Django Unfold: Use our colours instead of default Unfold colours.
- django-ckeditor-5
- Pillow
- WhiteNoise
- Gunicorn

Follow:

- PEP 8
- SOLID
- DRY
- Django Best Practices

---

# DEVELOPMENT RULES

- Build one Django app at a time.
- Complete each app before moving to the next.
- Ensure each app is fully integrated.
- Keep templates modular.
- Use reusable components.
- Write clean and maintainable code.
- Test functionality after every major feature.
- Do not generate placeholder code.
- Do not skip steps.
- Every feature should be production-ready.

---

# FINAL OBJECTIVE

The final result should be a premium humanitarian NGO website that communicates:

- Compassion
- Hope
- Transparency
- Professionalism
- Trust
- Global humanitarian impact

The website should inspire visitors to confidently support Blessed To Bless Humanity Aid through donations, volunteering, partnerships, and advocacy while remaining easy to manage through Django Admin.