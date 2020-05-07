import logging

# Configuration of logger
LOG_FORMAT = "%(levelname)s %(pathname)s %(funcName)s %(asctime)s - %(message)s"
logging.basicConfig(filename = 'report.log', 
					level=logging.DEBUG,
					format=LOG_FORMAT)


logger = logging.getLogger()