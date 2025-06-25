# 📸 Photographer Portfolio Website

This is a modern, responsive photographer portfolio website built using **Django**, **Bootstrap**, and **custom templates**. It allows photographers to showcase their work, manage content via a custom admin dashboard, and provide a professional online presence.

---

## 🔧 Features

- 📷 **Gallery System** – Upload and categorize photos with filtering support
- ✅ **Admin Dashboard** – Manage testimonials, FAQs, photos, and skills
- 💬 **Testimonials Section** – Display client feedback with images and titles
- 📖 **FAQs** – Frequently asked questions module
- 💼 **About and Skills Pages** – Highlight experience and areas of expertise
- 🎨 **Bootstrap-Based UI** – Mobile-responsive design with a modern look
- 🔐 **Authentication** – Custom user model using email login

---

## 📁 Project Structure

hollixplicits/
│
├── dashboard/ # Admin dashboard app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/dashboard/
│
├── portfolio/ # Public-facing app (home, gallery, etc.)
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/portfolio/
│
├── static/ # CSS, JS, and images
│
├── media/ # Uploaded media (testimonials, photos, etc.)
│
├── hollixplicits/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
└── README.md


