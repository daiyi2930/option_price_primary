#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:58:11 2019

@author: xizhou
"""

Jupyter QtConsole 4.4.3
Python 3.7.1 (default, Dec 14 2018, 13:28:58) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

from math import log,sqrt,exp

from scipy.stats import norm

def call(S,K,T,t,sigma,r):
    d1=(log(S/K)+(r+0.5*sigma*sigma)*(T-t))/sigma/sqrt(T-t)
    d2=d1-sigma*sqrt(T-t)
    call_price=S*norm.cdf(d1)-K*exp(-r*(T-t))*norm.cdf(d2)
    return call_price
    

def put(S,K,T,t,sigma,r):
    d1=(log(S/K)+(r+0.5*sigma*sigma)*(T-t))/sigma/sqrt(T-t)
    d2=d1-sigma*sqrt(T-t)
    put_price=K*exp(-r*(T-t))*norm.cdf(-d2)-S*norm.cdf(-d1)
    return put_price
    

call(100,100,0.5,0,0.2,0.01) #call3.1
Out[5]: 5.876024233827607

put(100,100,0.5,0,0.2,0.01) #put3.1
Out[6]: 5.377272153095845

call(100,120,0.5,0,0.2,0.01) #call 3.2 
Out[7]: 0.7741388057155696

put(100,120,0.5,0,0.2,0.01) #put 3.2
Out[8]: 20.175636308837454

call(100,100,1,0,0.2,0.01) #call 3.3
Out[9]: 8.433318690109608

put(100,100,1,0,0.2,0.01) #put 3.3
Out[10]: 7.438302065026413

call(100,100,0.5,0,0.3,0.01) #call 3.4
Out[11]: 8.677645562336004

put(100,100,0.5,0,0.3,0.01) #put 3.4
Out[12]: 8.178893481604248

call(100,100,0.5,0,0.2,0.02) #call3.5
Out[13]: 6.120654113455842

put(100,100,0.5,0,0.2,0.02) #put 3.5
Out[14]: 5.1256374883726465

#Strike for call:Except their different strike price,the call option3.1 and call option 3.2 are exactly the same.So by comparing the price of call option3.1(strike=100,price:5.876024233827607) and call option3.2(strike=120,price:0.7741388057155696),we could see that the call option with lower strike price would be more expensive,since it's more likely to be exercised.
#Strike for put:Put option,by contrast,with higher strike price would be more expensive since it's more likely to be exercised.We can see that by comparing the put option3.1(strike=100,price=5.377272153095845) with put option3.2(strike=120,price=20.175636308837454).
#Maturity:Except their different maturity date,the call/put option 3.1 (T=0.5)and the call/put option 3.3 (T=1.0)are exactly the same,by comparing the price of call/put option 3.1(call3.1=5.876024233827607;put3.1=5.377272153095845)with the price of call/put option 3.3(call3.3=8.433318690109608;put3.3=7.438302065026413)respectively,we could see that the option with longer maturity will be more expensive.
#Volatility:Except their different volatility,the call/put option 3.1 (sigma=0.2)and the call/put option 3.4 (sigma=0.3)are exactly the same,by comparing the price of call/put option 3.1(call3.1=5.876024233827607;put3.1=5.377272153095845)with the price of call/put option 3.4(call3.3=8.677645562336004;put3.3=8.178893481604248)respectively,we could see that the option with higher volatility will be more expensive.
#risk free rate for call:Except their different risk free rate,the call option 3.1(r=0.01)and the call option 3.5 are exactly same.By comparing the price of call3.1(price:5.876024233827607) and the price of call3.5(price:6.120654113455842),we could see for call option,the higher the risk free rate,the higher the call option value.
#risk free rate for put:On the contrary,for put option,the put option with lower risk free rate will be more expensive.We could see that by compare the put option3.1 and the put option3.5,these rwo option are exactly same except their risk free rate.put option3.1 (r=0.01,price=5.377272153095845)is more expensive than put option 3.5 (r=0.02,price=5.1256374883726465).
