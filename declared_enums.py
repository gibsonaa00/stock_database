from enum import Enum, auto

class Columns(Enum):
    CURRENCY=('currency', 'TEXT')
    SYMBOL=('symbol', 'TEXT')
    EXCHANGENAME=('exchangeName', 'TEXT')
    FULLEXCHANGENAME=('fullExchangeName', 'TEXT')
    INSTRUMENTTYPE=('instrumentType', 'TEXT')
    GMTOFFSET=('gmtoffset', 'INT')
    TIMEZONE=('timezone', 'TEXT')
    EXCHANGETIMEZONENAME=('exchangeTimezoneName', 'TEXT')
    FIFTYTWOWEEKHIGH=('fiftyTwoWeekHigh', 'REAL')
    FIFTYTWOWEEKLOW=('fiftyTwoWeekLow', 'REAL')
    SHORTNAME=('shortName', 'TEXT')
    CHARTPREVIOUSCLOSE=('chartPreviousClose', 'REAL')
    PRICEHINT=('priceHint', 'INT')
    START=('start', 'INT')
    END=('end', 'INT')
    TIMESTAMP=('timestamp', 'INT')
    DATE=('date', 'TEXT')
    CLOSE=('close', 'REAL')
    LOW=('low', 'REAL')
    OPEN=('open', 'REAL')
    VOLUME=('volume', 'INT')
    HIGH=('high', 'REAL')
    ADJCLOSE=('adjclose', 'REAL')
    ERROR=('error', 'TEXT')


class ScrapeMethod(int,Enum):
    ALL=auto() # requires no dates scrapes everything
    FROM=auto() # only require first date d1
    TO=auto() # only requires first date d1
    FROMTO = auto() # requires both dates d1 and d2