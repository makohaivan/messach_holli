import os
import sys
import django
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hollixplicits.settings')
django.setup()

# Now import Django settings and mail
from django.conf import settings
from django.core.mail import send_mail

def test_email():
    try:
        print("\n=== Testing Email ===")
        print(f"Using backend: {settings.EMAIL_BACKEND}")
        print(f"From: {settings.DEFAULT_FROM_EMAIL}")
        print(f"To: {settings.CONTACT_EMAIL}")
        
        send_mail(
            'Test Email Subject',
            'This is a test email body.',
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        print("SUCCESS: Email sent!")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    test_email()