import sys
import datetime
import time
import os
import urllib

SUSQPROXY = {'http': 'http://http-proxy.susq.com:80'}


def getsymbols(path='data/sp500.csv'):
    
    syms = []
    with open(path, 'r') as fh:
        for line in fh.readlines():
            if line == '':
                continue

            toks = line.split(',')

            sym = toks[0]

            if sym == '\n':
                continue
            syms.append(toks[0])

    return syms

def getdatafromyahoo(sym):
    url = "http://ichart.finance.yahoo.com/table.csv?s=%s&d=7&e=2&f=2011&g=d&a=8&b=7&c=1984&ignore=.csv" % sym
    urllib.urlretrieve(url, 'data/csv/sp500/%s.csv' % sym.lower())
    

if __name__ == '__main__':
    
    symbols = getsymbols()
    
    t1 = datetime.datetime.now()
    start = t1
    for symbol in symbols:
        getdatafromyahoo(symbol)
        print 'Getting data for %s (%d sec)' % (symbol, (datetime.datetime.now() - t1).seconds)
        t1 = datetime.datetime.now()

    print 'Total time: %d sec' % (datetime.datetime.now() - start).seconds
