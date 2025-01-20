import datetime, os

class PyLogger:
    """
    Simple logging class.

    Args:
        file (str): The file to saves logs to.
        format (str): The format of the log message.
    """
    def __init__(self, file='logs/app.log', format='%(asctime)s | %(levelname)s | %(message)s'):
        self.file = file
        self.format = format

    def log(self, lvl, *msg, file=None, format=None, prt=False):
        """
        Logs a message to a file.

        Args:
            lvl (str): Level of importance.
            *msg (str): The message(s) of the log.
            file (str, optional): The file to save to. Defaults to self.file.
            format (str, optional): The format of the log message. defaults to self.format.
            prt (bool, optional): Print to console. Defauls to False.
        """
        if file is None:
            file = self.file
        if format is None:
            format = self.format
        
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = ' '.join(str(m) for m in msg)
        log_entry = format.replace('%(levelname)s', lvl.upper()) \
                          .replace('%(asctime)s', timestamp) \
                          .replace('%(message)s', message)
        if prt:
            print(log_entry)
        directory = os.path.dirname(file)
        if directory and not os.path.exists(directory): # Check directory
                os.makedirs(directory)

        with open(file, 'a') as file:
            file.write(log_entry + '\n')

    def info(self, *msg, file=None, format=None, prt=False):
        "Logs as info"
        self.log('INFO', *msg, file=file, format=format, prt=prt)

    def warning(self, *msg, file=None, format=None, prt=False):
        "Logs as warning"
        self.log('WARNING', *msg, file=file, format=format, prt=prt)

    def error(self, *msg, file=None, format=None, prt=False):
        "Logs as error"
        self.log('ERROR', *msg, file=file, format=format, prt=prt)

    def debug(self, *msg, file=None, format=None, prt=False):
        "Logs as debug"
        self.log('DEBUG', *msg, file=file, format=format, prt=prt)