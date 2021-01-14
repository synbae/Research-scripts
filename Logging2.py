import logging

logging.basicConfig(filename="./Files/test1.log",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(levelname)-8s %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug('This is debug message')
logging.info('This is info message')

logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')