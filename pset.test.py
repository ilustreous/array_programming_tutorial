# <demo> silent

stop_here_for_problem = """Compute the standard deviation by symbol.

1) Imperative Programming style
2) Array Programming style

Bonus:
    1) Compute the standard deviation in the array 
       programming style in 1 line.

Take 15-20 min to work it out. 

Work with neighbors, use the internet.

BUT don't use numpy's builtin std function, nice try!


"""

print stop_here_for_problem

################
slidecounter() #
################
# <demo> stop

price_from_mean = closeprices - closeprices.mean(axis=0)



################
slidecounter() #
################
# <demo> stop

abs_price_from_mean = np.abs(price_from_mean)



################
slidecounter() #
################
# <demo> stop

abs_price_squared = abs_price_from_mean ** 2



################
slidecounter() #
################
# <demo> stop

mean_price_squred = np.mean( abs_price_squared, axis=0 )



################
slidecounter() #
################
# <demo> stop

std_prices = np.sqrt( mean_price_squred)



################
slidecounter() #
################
# <demo> stop

# oneliner to get std of prices
std_prices2 = np.sqrt( np.mean( np.abs(closeprices - closeprices.mean(axis=0)) ** 2 , axis=0 ))



################
slidecounter() #
################
# <demo> stop

# lets boxplot to visualize the stdev
fig  = plt.figure()
ax3 = fig.add_subplot(111)
ax3.boxplot(closeprices[:, ann_devs.argsort()[-1]], notch=0, sym='+', vert=1, whis=1.5, positions=None
        , widths=None, patch_artist=False)

ax3.set_title(symbols[ann_devs.argsort()][-1])

################
slidecounter() #
################
# <demo> stop
