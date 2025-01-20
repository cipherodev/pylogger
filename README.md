
# PyLogger

A simple python logger unlike the built in logging module.

## Features

- Log what you want to a file

## Requirements

- Python 3.0+

## Setup

1. Clone this repository

## Usage

```
from pylogger import PyLogger

logger = PyLogger(
    file='logs/app.log',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.debug('This is a debug message')
```

## License

MIT License
