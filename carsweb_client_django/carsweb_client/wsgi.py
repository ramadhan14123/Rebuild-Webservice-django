from django.core.wsgi import get_wsgi_application

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carsweb_client.settings')

application = get_wsgi_application()