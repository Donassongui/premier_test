# src/config.py

import os
from dotenv import load_dotenv

# Charge le .env depuis la racine du projet
load_dotenv()

# Base de données
DATABASE_URL = os.environ.get("DATABASE_URL")
DB_HOST      = os.environ.get("DB_HOST", "localhost")
DB_PORT      = int(os.environ.get("DB_PORT", 5432))
DB_NAME      = os.environ.get("DB_NAME")
DB_USER      = os.environ.get("DB_USER")
DB_PASSWORD  = os.environ.get("DB_PASSWORD")

# Sécurité
SECRET_KEY   = os.environ.get("SECRET_KEY")
DEBUG        = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

# Emails
EMAIL_HOST          = os.environ.get("EMAIL_HOST")
EMAIL_PORT          = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_HOST_USER     = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# APIs
OPENAI_API_KEY    = os.environ.get("OPENAI_API_KEY")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")

# AWS
AWS_ACCESS_KEY_ID      = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY  = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
