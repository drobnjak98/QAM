# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:34:24 2020

@author: User
"""


from numpy import zeros, array, random, floor, bitwise_xor

def modulator(data, M, G):
    a = array(range(int(2**(M/2))))
	
    for i in range(int(2**(M/2))):
        a[i]=G*((-(2**(M/2))+1)+2*i)
    vect = array(range(int(2**(M/2))))
    gray_code = bitwise_xor(vect, floor(vect/2).astype(int))

    data_input = data.reshape((-1,M))
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
    

    return I,Q

def noise(I, Q, G):
    noise = 1.3
    In = array(range(len(I)))
    Qn = array(range(len(Q)))
    for i in range(len(I)):
        In[i] = I[i]+ round(noise*G-2*noise*G* random.rand(),2)
    for i in range(len(Q)):
        Qn[i] = Q[i]+ round(noise*G-2*noise*G* random.rand(),2)
    return In,Qn