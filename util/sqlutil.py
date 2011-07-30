import classutil as cu
import os

def readfile(file_):
    #header: Date,Open,High,Low,Close,Volume,Adj Close
    import csv

    sym = file_.split(os.sep)[-1].split(".")[0]

    with open (file_, 'r') as fh:
        reader = csv.reader(fh)
        reader.next()
        for row in reader:
            if len(row) <= 0:
                continue
            row[0] = cu.str2epoch(row[0])
            row.insert(1, sym)
            yield row

def readfiles(globpattern):
    import glob
    csvfiles = glob.glob(globpattern)
    for csvfile in csvfiles:
        for line in readfile(csvfile):
            yield line

# create sql 
def sqlcreatetable(path=cu.fixpath('data/sqlite/histdatadb'), tablename='test'):
    import sqlite3
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.execute("""DROP TABLE IF EXISTS %(tablename)s""" % vars())

    cur.execute("""CREATE TABLE %(tablename)s (Date REAL
                                       ,Sym TEXT
                                       ,Open REAL
                                       ,High REAL
                                       ,Low REAL
                                       ,Close REAL
                                       ,Volume REAL
                                       ,AdjClose REAL)""" % vars())

    cur.execute("""CREATE INDEX dateidx_%(tablename)s ON %(tablename)s (Date)""" % vars())

    cur.execute("""CREATE INDEX symidx_%(tablename)s ON %(tablename)s (Sym)""" % vars())

    conn.commit()

    conn.close()


def sqlpopulatedata(files=cu.fixpath('data/csv/*.csv'), path=cu.fixpath('data/sqlite/histdatadb'), table='test', **kwargs):
    import sqlite3

    conn = sqlite3.connect(path)

    try:
        cur = conn.cursor()

        def insert(data, table, verbose=False):

            date = float(data[0])
            sym = data[1]
            open_ = float(data[2])
            high = float(data[3])
            low = float(data[4])
            close = float(data[5])
            volume = float(data[6])
            adjclose = float(data[7])
            
            insert = """
            INSERT INTO %(table)s (Date, Sym, Open, High, Low, Close, Volume, AdjClose)
            VALUES ('%(date)s', '%(sym)s', %(open_)s, %(high)s, %(low)s, %(close)s,
            %(volume)s, %(adjclose)s)
            """ % vars()

            if verbose:
                print insert

            cur.execute(insert)

        for line in readfiles(files):
            insert(line, table, **kwargs)

        conn.commit()
    finally:
        conn.close()

def sqlquery(sqlcmd="select * from prices", path=cu.fixpath('data/sqlite/histdatadb')):
    import sqlite3
    conn = sqlite3.connect(path)
    try:
        cur = conn.cursor()
        for row in cur.execute(sqlcmd):
            yield row
    finally:
        conn.close()

def sqlite2rec(query='select * from sp500', verbose=False, **kwargs):
    import numpy as np
    rowcountquery = 'select count(1) from (%s) a' % query 
    rowcount = [r for r in sqlquery(rowcountquery, **kwargs)][0][0]
    adtype = np.dtype([ ('date', float)
                    ,('sym', '|S4')
                    ,('open', float)
                    ,('high', float)
                    ,('low', float)
                    ,('close', float)
                    ,('volume', int)
                    ,('adjclose', float)])
    
    emptyrows = np.empty(rowcount, dtype=adtype)
    
    i = 0
    for row in sqlquery(query, **kwargs):
        emptyrows[i] = np.array(tuple(row), dtype=adtype)
        
        if verbose:
            if i % 10000 == 0:
                print '%d of %s' % (i, rowcount)
        i = i + 1

    return emptyrows.view(np.recarray)

def gethistprices(query, numrows=100):
    
    rec_arr = sqlite2rec(query)

    import matplotlib.mlab as mlab
    import numpy as np

    syms = np.unique(rec_arr.sym)

    xs = []

    for sym in syms:
        nosym = mlab.rec_drop_fields(rec_arr[rec_arr.sym == sym], ['sym',])
        
        xs.append(nosym[0:numrows].tolist())

    return (syms, xs)

