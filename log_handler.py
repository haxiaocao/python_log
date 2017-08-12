import logging
#import log_import_example  #this load the whole module , then the log_import_example.py run directly.

# Logging.NOTSET, Logging.DEBUG,Logging.INFO, Logging.WARNING,logging.ERROR,Logging.CRITICAL
logging.getLogger(__name__) : is the root logger , only one for ALL THE OTHER loggers.

logger =logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#handler=logging.StreamHandler()
handler=logging.FileHandler('log_handler.log')
handler.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


logger2=logging.getLogger(__name__)
handler2=logging.FileHandler("log_handler2.log")
handler2.setLevel(logging.WARNING)
formatter2=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler2.setFormatter(formatter2)

logger2.addHandler(handler2)
logger2.debug('debug message')
logger2.info('info message')
logger2.warn('warn message')
logger2.error('error message')
logger2.critical('critical message')
