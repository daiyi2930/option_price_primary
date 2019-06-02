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

#test
target_value=0.0004
c_or_p='C'
S=1.9585
K=2.40
Tminust=(8/365)
q=0.2
r=0.04
vol_ask=newton_sigma(target_value,c_or_p,S,K,Tminust,q,r)
print(vol_ask)

