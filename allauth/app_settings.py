from django.conf import settings


SITES_ENABLED = "django.contrib.sites" in settings.INSTALLED_APPS
SOCIALACCOUNT_ENABLED = "allauth.socialaccount" in settings.INSTALLED_APPS
SITE_ID = settings.SITE_ID

LOGIN_REDIRECT_URL = getattr(settings, "LOGIN_REDIRECT_URL", "/")

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")
