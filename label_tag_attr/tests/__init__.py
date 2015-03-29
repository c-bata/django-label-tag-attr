import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={"default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:"
    }}
)
settings.INSTALLED_APPS += ("label_tag_attr", )

django.setup()
