import sys
from dotenv import load_dotenv

print(f"Python Path: {sys.executable}")
print(f"Python Version: {sys.version}")

try:
    import dotenv
    load_dotenv()  # Actually load the environment
    print("SUCCESS! dotenv is working correctly")
    print(f"dotenv version: {dotenv.__version__}")  # Correct version check
except Exception as e:
    print(f"Error: {str(e)}")