from src.pylogger import PyLogger
#from pylogger import PyLogger

logger = PyLogger(
    file='logs/app.log',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.debug('This is a debug message')
