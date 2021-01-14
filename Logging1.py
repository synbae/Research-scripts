# Logging is a very useful tool in a programmer's toolbox. It can help you develop a better
# understanding of the flow of a program and discover scenarios that you might not even
# have though of while developing

# Log Levels
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL

import logging

logging.basicConfig(filename="./Files/test.log",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.DEBUG)

logging.debug('This is debug message')
logging.info('This is info message')

logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')