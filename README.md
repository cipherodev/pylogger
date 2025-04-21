
# PyLogger

A simple python logger unlike the built in logging module.

## Features

- Log what you want to a file

## Requirements

- Python 3.0+

## Setup

1. Clone this repository or download zip
```
git clone https://github.com/cipherodev/pylogger.git
```

## Usage

```python
from pylogger import PyLogger

log = PyLogger(
    file='logs/app.log',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

log.info('This is an info message')
log.warning('This is a warning message')
log.error('This is an error message')
log.debug('This is a debug message')
```

## License

MIT License
