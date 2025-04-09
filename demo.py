from src.pylogger import PyLogger
#from pylogger import PyLogger

log = PyLogger(
    file='logs/app.log',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

log.info('This is an info message')
log.warning('This is a warning message')
log.error('This is an error message')
log.debug('This is a debug message')
