import numpy as np

def testprices():
    x = np.array([ 35.438,35.75 ,35.875 ,36.938 ,39.313 
                  ,39.125 ,42.5 ,42.313 ,45.5 ,46.688 ,46.125 
                  ,43.75 ,45.375 ,46.594 ,46.938 ,46.188 
                  ,44.5 ,45.875 ,45.75 ,44.625 
                  ,45 ,45.5 ,48.375 ,51 ,47.75])
    y =           np.vstack([x,x])
    prices = y.transpose()
    return prices

def accumarray(arr, subs, func):
    
    uniqs = np.unique(subs)
    outarr = np.zeros((len(uniqs)))
    
    for x in uniqs:
        outarr[x] = func(arr[subs==x])
   
    return outarr


