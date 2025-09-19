# Symetric Encryption


In essance, it seems all the development is in regard that we cannot have a key of length equal to message,
it's technically possible, but it would be so inefficient. 

Thus the development has been to do create method/algorthim of which keys is a function that is, for each message consequenet message, a key is calculated. 

## Perfect Security: 

_Tries to answer what makes a cipher secured_

Check Shannon 1949, (it's why Dan called ciphers by Shannon) [Information theory] 

Conditions: 
 - P(E(k,m0),c) = P (E(k,m1),c) i.e. the probablity of random message m0,m1 (assume both 
 same length), in other words if we knoww c, we cannot know anything about m, or which m of 
 them is most likely to be given c.
 - l(k) >= l(m) which make it very unpractical e.g. for long message  

Notes:
- One time pad, is PC because we don't use the key again. **AND**
  length of the key `k` is at least or greater than `m`  
- For variable length time pad, it wouldn't work because the `c` length would 
  leak info about the length of the `m`  
- practicaly aim for high Pc and is perfect secureity isn't practical
- Change the key as frequent as could be (typically not starightforward in 
 hand of the end user)

## One-Time pad

Most straight forward form of encryption and is strong assuming is used only **once**.

The most important proetry is that size of `k` is equal to `m`. 

c = k ⊕ , m = k ⊕c 



