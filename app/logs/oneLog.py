import logging
import sys


# get logger
oneLogger = logging.getLogger()

# create formatter
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

# create handlers
streamHandler = logging.StreamHandler(sys.stdout)
fileHandler = logging.FileHandler("optinal.log")

# set formatter
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# add handlers to the logger
oneLogger.handlers = [streamHandler, fileHandler]

# set log-level
oneLogger.setLevel(logging.INFO)
