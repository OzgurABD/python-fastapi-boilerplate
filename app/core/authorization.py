from functools import wraps
from middlewares.exception import AuthException


def authorize(role: list):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            userRole = kwargs.get("currentUser")["role"]
            if userRole not in role:
                raise AuthException("User is not authorized")
            return await func(*args, **kwargs)

        return wrapper

    return decorator
