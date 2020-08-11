from logr import Logr
from levels import LevelDebug, LevelInfo, LevelNotice, LevelWarn, LevelError, LevelCrit, LevelAlert, LevelEmerg

conf = Logr(
    ('127.0.0.1', 7776),
    'MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFAMg7IrMCAwEAAQ==',
    'MC0CAQACBQDIOyKzAgMBAAECBQCHaZwRAgMA0nkCAwDziwIDAL+xAgJMKwICGq0=',
)


def test():
    logger = conf.getlogger('hello.log')
    for level in [LevelDebug, LevelInfo, LevelNotice, LevelWarn, LevelError, LevelCrit, LevelAlert, LevelEmerg, 'unknown']:
        logger.log(level, 'hello {}', 'python!', 123, [1, 2, 3], conf)

    counter = conf.getcounter('hello.log')


test()
