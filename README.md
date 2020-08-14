# logr-python-client


[Logr] client library for Python.

[Logr]: https://github.com/504dev/logr


    pip install logr-python-client

### Available `logger` methods

* `logger.emerg`
* `logger.alert`
* `logger.crit`
* `logger.error`
* `logger.warn`
* `logger.notice`
* `logger.info`
* `logger.debug`

### Available `counter` methods

* `counter.inc`
* `counter.avg`
* `counter.max`
* `counter.min`
* `counter.per`
* `counter.time`
* `counter.snippet` bonus method!


### Example

```python
from logr import Logr

conf = Logr(
    udp=('127.0.0.1', 7776),
    public_key='MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFAMg7IrMCAwEAAQ==',
    private_key='MC0CAQACBQDIOyKzAgMBAAECBQCHaZwRAgMA0nkCAwDziwIDAL+xAgJMKwICGq0=',
)

logger = conf.getlogger('hello.log')

# Send log
logger.info('Hello, Logr!')
logger.debug('It`s cool!')
```