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


from django.core.management import call_command

try:
    print("🚀 Faking migrations...")
    call_command('migrate', fake=True)
    print("✅ Migrations faked.")
except Exception as e:
    print("❌ Fake migration failed:", str(e))

