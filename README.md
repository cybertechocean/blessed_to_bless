# Blessed To Bless Humanity Aid (BBHA)

## Overview

Blessed To Bless Humanity Aid (BBHA) or rather "BLESSED TO BLESS" is a production-ready Django 6 web
platform for an international humanitarian NGO operating in the
Democratic Republic of Congo, Kenya, and Tanzania.

### Mission

Changing Lives. Restoring Hope. Empowering Communities.

## Tech Stack

-   Python 3.13+
-   Django 6.0.7
-   PostgreSQL
-   Tailwind CSS v4
-   HTMX
-   Alpine.js
-   Django Unfold
-   django-ckeditor-5
-   Pillow
-   WhiteNoise
-   Gunicorn

## Features

-   Responsive NGO website
-   English & French support
-   Programmes management
-   Emergency campaigns
-   Donation pages
-   News & Updates
-   Gallery
-   Contact forms
-   SEO optimization
-   Django Admin (Unfold): Use our colours instead of default Unfold colours.

## Planned Apps

-   core
-   accounts
-   pages
-   programs
-   campaigns
-   donations
-   gallery
-   news
-   contact
-   settings

## Project Structure

``` text
blessed_to_bless/
├── manage.py
├── blessed_to_bless/
├── core/
├── pages/
├── programs/
├── campaigns/
├── donations/
├── gallery/
├── news/
├── contact/
└── settings/
```

## Installation

``` bash
git clone <repository-url>
cd blessed_to_bless
python -m venv venv
```

Activate:

Windows:

``` powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run migrations:

``` bash
python manage.py migrate
```

Create superuser:

``` bash
python manage.py createsuperuser
```

Run server:

``` bash
python manage.py runserver
```

## Branding

Primary: `#00508E`

Accent: `#1E8F7A`

Background: `#FFFFFF`

Text: `#1F2937`

## Core Programmes

-   Emergency Relief
-   WASH
-   Healthcare
-   Education
-   Women Empowerment
-   Youth Development
-   Child Care & Protection
-   Elderly Support
-   Disability Inclusion
-   Livelihood Improvement
-   Disaster Response & Recovery
-   Community Development

## Deployment Checklist

-   DEBUG=False
-   Configure PostgreSQL
-   Collect static files
-   Configure WhiteNoise
-   Configure Gunicorn
-   Configure Nginx
-   Enable HTTPS
-   Set environment variables

## License

Copyright © Blessed To Bless Humanity Aid (BBHA). All rights reserved.
