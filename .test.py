from logr import Logr
from levels import LevelDebug, LevelInfo, LevelNotice, LevelWarn, LevelError, LevelCrit, LevelAlert, LevelEmerg

conf = Logr(
    udp=("127.0.0.1", 7776),
    public_key='MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFAMg7IrMCAwEAAQ==',
    private_key='MC0CAQACBQDIOyKzAgMBAAECBQCHaZwRAgMA0nkCAwDziwIDAL+xAgJMKwICGq0=',
)


def test():
    logger = conf.getlogger('hello.log')
    for level in [LevelDebug, LevelInfo, LevelNotice, LevelWarn, LevelError, LevelCrit, LevelAlert, LevelEmerg]:
        logger.log(level, 'hello {}', 'python!', 123, [1, 2, 3], conf)


test()
