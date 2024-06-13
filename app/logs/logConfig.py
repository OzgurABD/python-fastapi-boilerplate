# # Logging configuration
# import logging
# import logging.config
# import sys


# logging_config = {
#     "version": 1,
#     "formatters": {
#         "json": {
#             "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
#             "format": "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)s",
#         }
#     },
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "json",
#             "stream": sys.stderr,
#         }
#     },
#     "root": {"level": "DEBUG", "handlers": ["console"], "propagate": True},
# }

# logging.config.dictConfig(logging_config)

# https://medium.com/@dhavalsavalia/fastapi-logging-middleware-logging-requests-and-responses-with-ease-and-style-201b9aa4001a
