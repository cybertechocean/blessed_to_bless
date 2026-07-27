# Blessed To Bless Humanity Aid

This project is a Django 6 humanitarian NGO website for Blessed To Bless Humanity Aid (BBHA), serving communities in the Democratic Republic of Congo, Kenya and Tanzania.

## Running locally

Install the packages in `requirements.txt`, then run `python manage.py migrate` and `python manage.py runserver`. The Replit preview uses the configured `Start application` workflow on port 5000.

## Project notes

- Public pages and reusable templates live in `templates/core/`.
- The `core` app owns editable programmes, campaigns, news, gallery images, contact messages and volunteer applications.
- `logo.jpeg` is copied to `static/images/logo.jpeg` and is used in the header, footer and favicon.
- Content has thoughtful defaults so the public site renders before the first admin entries are created. Admin content overrides these defaults where applicable.

## User preferences

- Keep the existing Django stack and structure.
- Prefer a professional, accessible and mobile-first humanitarian design.