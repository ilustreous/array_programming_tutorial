import util
import numpy as np


def stdcalc1(closeprices):
    
    price_from_mean = closeprices - closeprices.mean(axis=0)

    abs_price_from_mean = np.abs(price_from_mean)

    abs_price_squared = abs_price_from_mean ** 2

    mean_price_squred = np.mean( abs_price_squared, axis=0 )

    std_prices = np.sqrt( mean_price_squred)

    return std_prices


def stdcalc2(closeprices):

    std_prices2 = np.sqrt( np.mean( np.abs(closeprices - closeprices.mean(axis=0)) ** 2 , axis=0 ))

    return std_prices2

def stdcalcnp(closeprices):

    return np.std(closeprices, axis=0)


def stdcalcreg(closeprices):
     
    mean = sum(closeprices) / len(closeprices)
    
    prices_from_mean = [closeprice - mean for closeprice in closeprices]
    
    abs_prices_from_mean = [abs(price_from_mean) for price_from_mean in prices_from_mean]

    abs_prcs_sqr_frm_mean = [abs_prc_frm_mean ** 2 for abs_prc_frm_mean in abs_prices_from_mean]
   
    mean_price_sqr =    sum(abs_prcs_sqr_frm_mean) / len(abs_prcs_sqr_frm_mean)
    
    std_price = mean_price_sqr ** .5

    return std_price

def stdcalcregall(symbols, closeprices):
    
    stdcalcs = []
    for symbol in symbols.tolist():

        std = stdcalcreg(closeprices[:,symbols == symbol].T.tolist()[0])
        stdcalcs.append(std)

    return stdcalcs


if __name__ == '__main__':


    sqltable = 'sp500_small' if util.is32bit() else 'sp500'

    query = 'select * from %(sqltable)s order by date desc' % vars()

    (symbols, prices) = util.gethistprices(query, numrows=1000, verbose=True)

    ADJCLOSE = 6

    closeprices = prices[:, :, ADJCLOSE].transpose()
    
    std_1 = stdcalc1(closeprices)
    
    std_2 = stdcalc2(closeprices)

    std_np = stdcalcnp(closeprices)

    std_reg = stdcalcregall(symbols, closeprices)
    
    # is std_1 the same as std_2
    is_std1_2_same = np.allclose(std_1, std_2)
    
    # is std_1 the same as std_np 
    is_std1_np_same = np.allclose(std_1, std_np)
    
    # is std_reg the same as std_np
    is_stdreg_np_same = np.allclose(std_np, np.array(std_reg))


    import cProfile

    std_1_prof = cProfile.Profile()
    std_1_prof.runcall(stdcalc1, closeprices)
    std_1_prof.dump_stats('stdcalc1.stats')

    std_2_prof = cProfile.Profile()
    std_2_prof.runcall(stdcalc2, closeprices)
    std_2_prof.dump_stats('stdcalc2.stats')

    std_np_prof = cProfile.Profile()
    std_np_prof.runcall(stdcalcnp, closeprices)
    std_np_prof.dump_stats('stdcalcnp.stats')

    std_reg_prof = cProfile.Profile()
    std_reg_prof.runcall(stdcalcregall, symbols, closeprices)
    std_reg_prof.dump_stats('stdcalcreg.stats')


    
