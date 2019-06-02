import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import log,sqrt,exp
from scipy.stats import norm


def option_price(c_or_p,S,K,Tminust,q,sigma,r):
    d1=(log(S/K)+(r-q+0.5*sigma*sigma)*Tminust)/sigma/sqrt(Tminust)
    d2=d1-sigma*sqrt(Tminust)
    if c_or_p =='C':
        div_option_price=S*exp(-q*(Tminust))*norm.cdf(d1)-K*exp(-r*(Tminust))*norm.cdf(d2)
    else:
        div_option_price=K*exp(-r*(Tminust))*norm.cdf(-d2)-S*exp(-q*(Tminust))*norm.cdf(-d1)
    return div_option_price
def vega(S,K,Tminust,q,sigma,r):
    d1=(log(S/K)+(r-q+0.5*sigma*sigma)*(Tminust))/sigma/sqrt(Tminust)
    vega=S*exp(-q*(Tminust))*sqrt(Tminust)*norm.pdf(d1)
    return vega

def newton_sigma(target_value,c_or_p,S,K,Tminust,q,r):
    sigmahat=sqrt(2*abs((log(S/K)+(r-q)*(Tminust))/(Tminust)))#starting value
    max_interations=100
    tolerance=10**-8
    sigmadiff=1
    sigma=sigmahat
    for i in range(1,max_interations):
        if(abs(sigmadiff)>=tolerance):
            price=option_price(c_or_p,S,K,Tminust,q,sigma,r)
            Vega=vega(S,K,Tminust,q,sigma,r)
            increment=(price-target_value)/Vega
            sigma=sigma-increment
            i=i+1
            sigmadiff=abs(increment)
        else:    
            return sigma

#for spot price at 09:31:00,we use the average of the bid/ask prices.A50's ask/bid price at 09:33 is 1.959 & 1.958 respectively,the average is 1.9585;
#From the data,we could know the expiry date is 2016-02-24,and the spot date is 2016-02-16,thus the T-t=8/365;
#for 09:31:00
snapshot_31=pd.read_csv('snapshot_31.csv')

print(snapshot_31)
option_31_bid=list(snapshot_31.iloc[:,4]) 
option_31_ask=list(snapshot_31.iloc[:,5]) 
strike_31=list(snapshot_31.iloc[:,2])
optiontype_31=list(snapshot_31.iloc[:,3])

for i in range(len(option_31_ask)):
    target_value=option_31_ask[i]
    c_or_p=optiontype_31[i]
    S=1.9585
    K=strike_31[i]
    Tminust=(8/365)
    q=0.2
    r=0.04
    vol_ask=newton_sigma(target_value,c_or_p,S,K,Tminust,q,r)
    print(vol_ask)

print('\n')
for i in range(len(option_31_bid)):
    target_value=option_31_bid[i]
    c_or_p=optiontype_31[i]
    S=1.9585
    K=strike_31[i]
    Tminust=(8/365)
    q=0.2
    r=0.04
    vol_bid=newton_sigma(target_value,c_or_p,S,K,Tminust,q,r)
    print(vol_bid)

#for spot price at 09:32:00,we use the average of the bid/ask prices.A50's ask/bid price at 09:33 is 1.957 & 1.956 respectively,the average is 1.9565;
#From the data,we could know the expiry date is 2016-02-24,and the spot date is 2016-02-16,thus the T-t=8/365;
#for 09:32:00
snapshot_32=pd.read_csv('snapshot_32.csv')
print(snapshot_32)

option_32_bid=list(snapshot_32.iloc[:,4]) 
option_32_ask=list(snapshot_32.iloc[:,5]) 
strike_32=list(snapshot_32.iloc[:,2])
optiontype_32=list(snapshot_32.iloc[:,3])

for i in range(len(option_32_ask)):
    target_value=option_32_ask[i]
    c_or_p=optiontype_32[i]
    S=1.9565
    K=strike_32[i]
    Tminust=(8/365)
    q=0.2
    r=0.04
    vol_ask=newton_sigma(target_value,c_or_p,S,K,Tminust,q,r)
    print(vol_ask)


print('\n')
for i in range(len(option_32_bid)):
    target_value=option_32_bid[i]
    c_or_p=optiontype_32[i]
    S=1.9565
    K=strike_32[i]
    Tminust=(8/365)
    q=0.2
    r=0.04
    vol_bid=newton_sigma(target_value,c_or_p,S,K,Tminust,q,r)
    print(vol_bid)

#for spot price at 09:33:00,we use the average of the bid/ask prices.A50's ask/bid price at 09:33 is 1.959 & 1.958 respectively,the average is 1.9585;
#From the data,we could know the expiry date is 2016-02-24,and the spot date is 2016-02-16,thus the T-t=8/365;
#for 09:33:00

snapshot_33=pd.read_csv('snapshot_33.csv')
print(snapshot_33)

option_33_bid=list(snapshot_33.iloc[:,4]) 
option_33_ask=list(snapshot_33.iloc[:,5]) 
strike_33=list(snapshot_33.iloc[:,2])
optiontype_33=list(snapshot_33.iloc[:,3])

for i in range(len(option_33_ask)):
    target_value=option_33_ask[i]
    c_or_p=optiontype_33[i]
    S=1.9585
    K=strike_33[i]
    Tminust=(8/365)
    q=0.2
    r=0.04
    vol_ask=newton_sigma(target_value,c_or_p,S,K,Tminust,q,r)
    print(vol_ask)

print('\n')
for i in range(len(option_33_bid)):
    target_value=option_33_bid[i]
    c_or_p=optiontype_33[i]
    S=1.9585
    K=strike_33[i]
    Tminust=(8/365)
    q=0.2
    r=0.04
    vol_bid=newton_sigma(target_value,c_or_p,S,K,Tminust,q,r)
    print(vol_bid)
