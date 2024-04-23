#ctbot_backend/ctbot_backend/asgi.py

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ctbot_backend.settings')

application = get_asgi_application()
