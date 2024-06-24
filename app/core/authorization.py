from functools import wraps
from middlewares.exception import AuthException


def authorize(role: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            userRoles = kwargs.get("currentUser")["roles"]
            if role not in userRoles:
                raise AuthException("User is not authorized", "AUR.001")
            return await func(*args, **kwargs)

        return wrapper

    return decorator
