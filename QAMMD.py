# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:42:57 2020

@author: User
"""


from numpy import  zeros, array, random, sqrt, floor, bitwise_xor
from numpy.random import randint

symbol_num = 20
M = 8
G = 1

data_input = randint(2, size=M*symbol_num)
data_input

a = array(range(int(2**(M/2))))

for i in range(int(2**(M/2))):
    a[i]=G*((-(2**(M/2))+1)+2*i)
a
    
vect = array(range(int(2**(M/2))))
gray_code = bitwise_xor(vect, floor(vect/2).astype(int))
gray_code

data_input = data_input.reshape((-1,M))
data_input

I = zeros((data_input.shape[0],))
Q = zeros((data_input.shape[0],))
for n in range(int(data_input.shape[1] / 2)):
    I = I + data_input[:,n] * 2 ** (int(data_input.shape[1]/2)-1-n)
for n in range(int(data_input.shape[1]/2),int(data_input.shape[1])):
    Q = Q + data_input[:,n] * 2 ** (int(data_input.shape[1])-1-n)

I = I.astype(int)
Q = Q.astype(int)

I = gray_code[I]
Q = gray_code[Q]
I = a[I]
Q = a[Q]

I = I.astype(float)
Q = Q.astype(float)

S = I + 1j * Q
S

noise = 1.3
In = array(range(len(I)))
Qn = array(range(len(Q)))
In = In.astype(float)
Qn = Qn.astype(float)
for i in range(len(I)):
    In[i] = I[i]+ round(noise*G-2*noise*G* random.rand(),2)
for i in range(len(Q)):
    Qn[i] = Q[i]+ round(noise*G-2*noise*G* random.rand(),2)
    
Sn = In + 1j * Qn
Sn

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
Sd=Id + 1j* Qd
Sd

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
data_exit

from QAMmodulator import modulator

I,Q = modulator(data_input, M, G)
S = I + 1j * Q
S

from QAMmodulator import noise

In,Qn = noise(I, Q, G)
Sn = In + 1j * Qn
Sn

from QAMdemodulator import demodulator

data_exit = demodulator(I, Q, In, Qn, M, G)
data_exit