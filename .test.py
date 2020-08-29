import random
from logrpy import Logr
from logrpy.levels import LevelDebug, LevelInfo, LevelNotice, LevelWarn, LevelError, LevelCrit, LevelAlert, LevelEmerg

conf = Logr(
    ('127.0.0.1', 7776),
    'MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFAMg7IrMCAwEAAQ==',
    'MC0CAQACBQDIOyKzAgMBAAECBQCHaZwRAgMA0nkCAwDziwIDAL+xAgJMKwICGq0=',
)


def test():
    logger = conf.getlogger('hello.log')
    for level in [LevelDebug, LevelInfo, LevelNotice, LevelWarn, LevelError, LevelCrit, LevelAlert, LevelEmerg,
                  'unknown']:
        logger.log(level, 'hello {}', 'python!', 123, [1, 2, 3], conf)

    logger.counter.watchsystem()
    logger.counter.inc('lol').avg(random.randint(0, 100))
    logger.info('Its Widget, Bro!', conf.getcounter('crypto.log').snippet('max', 'price:BTC_USDT', 30))


test()
