# Fuck logging module
import datetime, os

class Logger:
    """Logging class because the built in logging module is shit."""
    def __init__(self, file='logs/app.log', format='%(levelname)s | %(asctime)s | %(message)s'):
        self.file = file
        self.format = format

    def log(self, lvl, *msg, file=None, format=None, prt=False):
        """
        Log a message to a file and it's level of importance.
        Print to console if prt is True.
        Default to the class's file and format if None is provided.
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

        # append the message to file
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

