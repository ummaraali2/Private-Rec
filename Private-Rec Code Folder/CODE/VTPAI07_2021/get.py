import math as m
import random as r
  
def Hashgen() : 
  
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hcode = "" 
    varlen= len(string) 
    for i in range(16) : 
        hcode += string[m.floor(r.random() * varlen)] 
  
    return (hcode)

def getId():
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    uid = ""
    vlen = len(string)
    for i in range(3):
        uid += string[m.floor(r.random() * vlen)] 
    st = '0123456789'
    slen = len(st)
    for i in range(6):
        uid += st[m.floor(r.random() * slen)]
    return uid
        