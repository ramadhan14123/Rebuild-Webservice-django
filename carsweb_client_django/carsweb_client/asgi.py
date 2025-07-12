from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carsweb_client.settings')

application = get_asgi_application()