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


# ✅ Run migrations manually (only temporarily!)
from django.core.management import call_command

try:
    print("🚀 Applying migrations...")
    call_command('migrate', interactive=False)
    print("✅ Migrations applied.")
except Exception as e:
    print("❌ Migration failed:", str(e))