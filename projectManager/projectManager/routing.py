from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from chat import routing
from notification import routing as notificationr
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(
        routing.websocket_urlpatterns + notificationr.urlpatterns
        
    ))
})