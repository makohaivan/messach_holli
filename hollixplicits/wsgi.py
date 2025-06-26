"""
WSGI config for hollixplicits project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hollixplicits.settings')

application = get_wsgi_application()


# ✅ TEMP: Fix for missing tables in PostgreSQL
from django.db import connection
from django.core.management import call_command

try:
    print("🔥 Deleting migration history...")
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM django_migrations;")
    print("✅ Migration history cleared.")

    print("🚀 Applying migrations...")
    call_command('migrate', interactive=False)
    print("✅ Migrations applied.")
except Exception as e:
    print("❌ Migration error:", str(e))
