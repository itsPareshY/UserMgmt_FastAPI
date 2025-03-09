# app/routes/__init__.py
# Import all route modules to make them available when importing 'routes'

from .auth import router as auth_router
from .users import router as users_router
from .admin import router as admin_router
from .security import router as security_router
from .notifications import router as notifications_router

# List of all registered routers
__all__ = ["auth_router", "users_router", "admin_router", "security_router", "notifications_router"]
