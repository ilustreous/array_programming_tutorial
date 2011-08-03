import classutil as cu
import dateutil as du
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
            row[0] = du.str2epoch(row[0])
            row.insert(1, sym)
            yield row

def readfiles(globpattern):
    import glob
    csvfiles = glob.glob(globpattern)
    for csvfile in csvfiles:
        for line in readfile(csvfile):
            yield line

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

def sqlite2dict(query='select * from sp500', verbose=False, **kwargs):
    import collections
    ts = collections.defaultdict(list) 
    for row in sqlquery(query, **kwargs): 
        ts[row[1]].append(row)
    return ts

def sqlite2rec(query='select * from sp500', verbose=False, **kwargs):
    import numpy as np

    rowcountquery = 'select count(1) from (%s) a' % query.replace('order by date desc', '')

    rowcount = [r for r in sqlquery(rowcountquery, **kwargs)][0][0]

    print 'Row count = %d' % rowcount

    adtype = np.dtype([ ('date', float)
                    ,('sym', '|S4')
                    ,('open', float)
                    ,('high', float)
                    ,('low', float)
                    ,('close', float)
                    ,('volume', int)
                    ,('adjclose', float)])
    
    emptyrows = np.empty(rowcount, dtype=adtype)
    
    ts = []
    start = 0
    step = 250000
    for row in sqlquery(query, **kwargs): 
        ts.append(row)
        
        if len(ts) == step:
            stop = start + step
            #print 'start:%d\nstop:%d' % (start, stop)
            # go from start to stop excluding stop
            emptyrows[start:stop] = np.array(ts, dtype=adtype)
            start = stop
            ts = []

            if verbose:
                if start % step == 0:
                    print '%d of %s rows' % (start, rowcount)

    if len(ts) > 0:
        emptyrows[start:start+len(ts)] = np.array(ts, dtype=adtype)

    return emptyrows.view(np.recarray)

def sqlite2recslow(query='select * from sp500', verbose=False, **kwargs):
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
        emptyrows[i] = np.array(row, dtype=adtype)
        if verbose:
            if i % 250000 == 0:
                print '%d of %s rows' % (i, rowcount)

        i += 1

    return emptyrows.view(np.recarray)

def gethistprices(query, numrows=1000, **kwargs):
    
    rec_arr = sqlite2rec(query, **kwargs)

    import matplotlib.mlab as mlab
    
    import numpy as np

    (syms, posuniq, pos) = np.unique(rec_arr.sym, True, True)
    
    new_rec_arr = mlab.rec_append_fields(rec_arr, 'idx', pos)
    
    nosym = mlab.rec_drop_fields(new_rec_arr, ['sym',])
    
    recnumrecs = mlab.rec_groupby(nosym, ('idx',), (('idx', len, 'idxcount'), ))

    idx = np.nonzero(recnumrecs.idxcount >= numrows)[0]

    idxcount = len(recnumrecs[idx])

    xs = np.empty((idxcount, numrows, len(nosym[0])-1), dtype=float)

    for i in xrange(idxcount):

        if kwargs.has_key('verbose') and kwargs['verbose'] and i % 50 == 0:
            print '%d of %d' % (i, idxcount)
        
        curdata = nosym[nosym.idx == idx[i]]

        curdata_arr = np.array(curdata.tolist(), dtype=float)
        xs[i] = curdata_arr[0:numrows:,0:-1]
        
    return (syms[idx], xs)



#run getdataforsymbols.py
#util.sqlcreatetable(tablename='sp500')
#cd data/csv/sp500
#ls | xargs grep '404 Not Found' | gawk -F':' '{print $1}' | xargs rm
#util.sqlpopulatedata(files=utilfixpath('data/csv/sp500/*.csv'), table='sp500')
