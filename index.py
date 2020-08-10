from logr import Logr

conf = Logr(
    udp=("127.0.0.1", 7776),
    public_key='MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFAMg7IrMCAwEAAQ==',
    private_key='MC0CAQACBQDIOyKzAgMBAAECBQCHaZwRAgMA0nkCAwDziwIDAL+xAgJMKwICGq0=',
)

logger = conf.getlogger('hello.log')

logger.info('hello {}', 'python!', 123, [1, 2, 3], conf)
