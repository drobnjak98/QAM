# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:37:36 2020

@author: User
"""
from numpy import array, sqrt, floor, bitwise_xor

def demodulator(I, Q, In, Qn, M, G):

    a = array(range(int(2**(M/2))))
    for i in range(int(2**(M/2))):
        a[i]=G*((-(2**(M/2))+1)+2*i)
    vect = array(range(int(2**(M/2))))
    gray_code = bitwise_xor(vect, floor(vect/2).astype(int))
    
    Id=I
    Qd=Q
    amax=int(2**(M/2)-1)
    for i in range(len(I)):
        if Id[i]!=a[0] and Qd[i]!=a[amax]:
            if sqrt((Id[i]-In[i])**2 + (Qd[i]-Qn[i])**2) > sqrt((Id[i]-2*G-In[i])**2 + (Qd[i]+2*G-Qn[i])**2):
                Id[i]=Id[i]-2*G
                Qd[i]=Qd[i]+2*G
        if Qd[i]!=a[amax]:
            if sqrt((Id[i]-In[i])**2 + (Qd[i]-Qn[i])**2) > sqrt((Id[i]-In[i])**2 + (Qd[i]+2*G-Qn[i])**2):
                Id[i]=Id[i]
                Qd[i]=Qd[i]+2*G
        if Id[i]!=a[amax] and Qd[i]!=a[amax]:
            if sqrt((Id[i]-In[i])**2 + (Qd[i]-Qn[i])**2) > sqrt((Id[i]+2*G-In[i])**2 + (Qd[i]+2*G-Qn[i])**2):
                Id[i]=Id[i]+2*G
                Qd[i]=Qd[i]+2*G
        if Id[i]!=a[amax]:
            if sqrt((Id[i]-In[i])**2 + (Qd[i]-Qn[i])**2) > sqrt((Id[i]+2*G-In[i])**2 + (Qd[i]-Qn[i])**2):
                Id[i]=Id[i]+2*G
                Qd[i]=Qd[i]
        if Id[i]!=a[amax] and Qd[i]!=a[0]:
            if sqrt((Id[i]-In[i])**2 + (Qd[i]-Qn[i])**2) > sqrt((Id[i]+2*G-In[i])**2 + (Qd[i]-2*G-Qn[i])**2):
                Id[i]=Id[i]+2*G
                Qd[i]=Qd[i]-2*G
        if Qd[i]!=a[0]:
            if sqrt((Id[i]-In[i])**2 + (Qd[i]-Qn[i])**2) > sqrt((Id[i]-In[i])**2 + (Qd[i]-2*G-Qn[i])**2):
                Id[i]=Id[i]
                Qd[i]=Qd[i]-2*G
        if Id[i]!=a[0] and Qd[i]!=a[0]:
            if sqrt((Id[i]-In[i])**2 + (Qd[i]-Qn[i])**2) > sqrt((Id[i]-2*G-In[i])**2 + (Qd[i]-2*G-Qn[i])**2):
                Id[i]=Id[i]-2*G
                Qd[i]=Qd[i]-2*G
        if Id[i]!=a[0]:
            if sqrt((Id[i]-In[i])**2 + (Qd[i]-Qn[i])**2) > sqrt((Id[i]-2*G-In[i])**2 + (Qd[i]-Qn[i])**2):
                Id[i]=Id[i]-2*G
                Qd[i]=Qd[i]
                
    Id=Id.astype(int)
    Qd=Qd.astype(int)
    dictnums={}
    for i in range(int(2**(M/2))):
        dictnums.update({a[i] : i})
    for i in range(len(I)):
        Id[i]=dictnums.get(Id[i])
        Qd[i]=dictnums.get(Qd[i])
    dictbits={}
    for i in range(int(2**(M/2))):
        dictbits.update({gray_code[i] : i})
    for i in range(len(I)):
        Id[i]=dictbits.get(Id[i])
        Qd[i]=dictbits.get(Qd[i])
    
    data_exit=[]
    for i in range(len(Id)):
        e=[]
        x=0
        while x < M/2:
            b= Id[i] % 2
            e.append(b)
            Id[i]=Id[i]/2
            x=x+1
        e.reverse()
        data_exit.extend(e)
        f=[]
        y=0
        while y < M/2:
            c= Qd[i] % 2
            f.append(c)
            Qd[i]=Qd[i]/2
            y=y+1
        f.reverse()
        data_exit.extend(f)
    data_exit=array(data_exit)
    return data_exit
