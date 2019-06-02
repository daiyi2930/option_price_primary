import scipy as sp
import numpy as np

x=sp.random.normal(0,1,200)

y=sp.random.normal(0,1,200)

import math

from math import sqrt

z=0.5*x+(sqrt(1-0.5*0.5))*y

from scipy import stats
test_x=sp.stats.normaltest(x,axis=0)
test_y=sp.stats.normaltest(y,axis=0)
print(test_y)
print(test_x)
'''NormaltestResult(statistic=0.4219250188256409, pvalue=0.8098044263556202)
NormaltestResult(statistic=2.8710514859951415, pvalue=0.2379902094318978)
'''

coefficient_xz=np.corrcoef(x,z)
print(coefficient_xz)

'''output:
[[1.         0.50600392]
 [0.50600392 1.        ]]
the coefficient of x and z is 0.5 (see the output above),same as the theoretical value 0.5.
'''




