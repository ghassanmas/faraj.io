# Symetric Encryption


In essance, it seems all the development is in regard that we cannot have a key of length equal to message,
it's technically possible, but it would be so inefficient. 

Thus the development has been to do create method/algorthim of which keys is a function that is, for each message consequenet message, a key is calculated. Also randomization plays a key role if not the cort of it.


## Perfect Security: 

_Tries to answer what makes a cipher secured_

Check Shannon 1949, (it's why Dan called ciphers by Shannon) [Information theory] 

Conditions: 
 1. P(E(k,m0),c) = P (E(k,m1),c) i.e. the probablity of random message m0,m1 (assume both 
 same length), in other words if we know c, we cannot know anything about m, or which M of 
 them is most likely to be given c.
 2. l(k) >= l(m) which make it very unpractical e.g. for long message  
 3. otehr way to put given M(m0...mn) and C(c0,cn), taken cx at random, would have equal probabliity
 distrubuted among elemnts of M.
 4. **Need to revist**: > Key space K, has to be as large as large as M space 
   - ~~It would weaken aginst an attack of which trying to guess the `k`~~(maybe), it's evntual 
    that a key could decrypt one or message, i.e `D(cx,kx)= mx`  `D(cy,ky) = my`
     where ky,kx were picked at random, but we were out of randomness, given the M
     turned out to be large than K 
5. Following previous point, although _for reason that will come lateR_, E(m,k), or C
  space is random. how this space randomniess ralte to previous one or Ps will come
  later
6. ~~4 and 5 suppose to indpendent of each other, p8^~~ it suppose to K and M, mau be 4 
 and 5, not clear yet.
7. The indpenance between spaces to each other K,M and C plys a key role, in determining if it's
 prefectly secure or what degree is it. The K space being the most restrictive, understandbaly as
 it's used with combination of M, of which we cannot guarante (in typical consuming apps), that m
 is not dublicated. (e.g. short message)

K,C 
K,M
C,M

Notes:
- One time pad, is Ps because we don't use the key again. **AND**
  length of the key `k` is at least equal or greater than `m`  
- For variable length time pad, it wouldn't work because the `c` length would 
  leak info about the length of the `m`.  
- practicaly aim for high Pc, and is perfect secureity isn't practical
- Change the key as frequent as could be (typically not starightforward or not in 
 hand of the end user) Adv
- Don't send same messge over and over again as it would minizie the unifromaity of space M

## Ciphers
### 3.1 One-Time pad

Most straight forward form of encryption and is strong assuming is used only **once**.

The most important proetry is that size of `k` is equal to `m`. 

c = k ⊕ , m = k ⊕ c 

Note: the length of the key one time pad not necessarly same length as message
hence, is the cipher for perfect secuerty. 


