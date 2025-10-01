# Symetric Encryption


In essance, it seems all the development is in regard that we cannot have a key of length equal to message,
it's technically possible, but it would be so inefficient. 

Thus the development has been to do create method/algorthim of which keys is a function that is, for each message consequenet message, a key is calculated. Also randomization plays a key role if not the cort of it.

Indeed randomization is important, it's necessarly so that `k` is uniformely disturbted among K.


## Perfect Security: 


Todo: rephase statement i,ii,ii @p9
-------


i _just assume it's secure so the rest point make sense_?

ii: 
 if we iterate over all messages, then the probability that a given
 cipher belongs a key `k` of K, is constant among all memebers of m. 

 For that to be true, the number of `k` that map to a spesfic c, is 
 same among all memebers of m. (in case of one time pad, its one
 because as name state **one** time pad). 

iii: 
  if by any chance space of K has a probaility of (2 = / |K|),
   meaning for _any random chosen k of K, there is other
   identiacl k_. then to get the same ratio of C either: 
         - then |M| <= |K| / 2.
  

One time is easy to reason in the book, beceause we assume |K| = 
|M| = |C| thus NC must be exctly 1.

This demands the key not to be shorter than message, to be secured, 
because then we won't have same distribution of C as in K, e.g. in 
case of variable length one time pad. Is obvious for short message
we will have more than one `k` that leads to `C`, because
 
 if we are cutting `k`, then eventually more than one memeber 
 of k will lead to c, consider example 
  i0: 11111100 (1: use k[i], 0: drop k[i]) 
  k0: 01011011 (assume we use this for m0)
  k1: 01011001 (assume we use this for m1)
  k2: 01011110 
  k3: 01011100
  m0: 010111   (an example m0 with length 6) 
  c0: 000001   (cipher has same length 6)
  
  i1: 11111111 (all of them are used)
  k1: 01011001
  m1: 01101011 
  c1: 00110010
  
  meaning we have 4 keys that would lead to c given m.
  and then if m1 length equal k, then only one k could 
  lead to m1. Then this conflict with ii, becuase NC 
  of c0 4 =/= 1 Nc of m1.
  
  taking equation of ii into consdiration given
  c0, NC = 4 (there are 4 keys that can lead c0)
  
  while for m1 we only have one key NC = 1 
  Thus NC is not consitent among the Ms, thus it's
  not perefect secure.

  even worse for this example, k1 would work for 
  both. But even if the k of m1, wasn't of the 
  keys variant of m0/c0 it's still not secure. 

  one case variable lenght one time pad, would
  work, if we gurante, that all memebers of M
  have the same length that is equal to length 
  k, but then we are back to classic one time
  pad. 

** Start of Question 1**
Q1: relate to ii[i], if M is larger than
 K, proof that it's not perfectly secure?

 if M > K, then we are sure at least 
 one of `k` is being used twice.
 
 but then what info or connection can that help 
 to distugish m or c form others? 

 Also how does that affect the distrubtion of c
 among C.

  The only case we can get more memebers of |K| than
  memebers of |M| would be if either of below statements
  is true
  1: We sent too many messages; thus k is no longer 
  unfirmely disturubted
  2: memebers of K aren't uniformely distrubted

  A1A: we sent too many messages
  In case the cipher is one time pad, then we 
  are certian that one of the M is duplicate.
  because we assume K is uniformely distrubted
  thus, IT MUST BE that one of message is being
  sent twice*. 
  And if we already have exhausted all memebers of K
  then we also have a duplicate in c (hence iii).
  And if we have a duplcate in `c`. Then there must be 
  one of the `m` of which it would produce same `c` with
  two different key. Thus breaking Nc of equation ii. 

  so then given ii, Nc of the duplicate m would 
  be 2 while for the other is 1. 

 *And even worse, because human created langauges
 don't distrube characters unifomrely among the
 set of characters or alphates, in a setnance.
 for example consider the pair of k,m (written in ASCII)
 m: hoiaer aertiopj aserpojs  (No way this English sentance)
 k: kllinalkenrlkanwralkjnwrl (has same probabiilty as other k)

 A1B: Case of K aren't unfiformely distrubted).
 When memebrs of K, aren't uniformarluy distrubted
 this could mean that one key would appear more times
 than other keys. Thus we have high proability a key
 is being resued. given iii, then C also has same 
 distribution, meaning we will end with duplciate c
 which would also break Nc of equation ii.

 From practical prespesctive though, if we are using
 one time pad, a key is being reused then it's no longer
 one time pad. 

 --Trivia Q1---
 Another way to intrupet being not uniformely distrubted
 is that not necessary we have duplciate k, but one of k has
 more chance of appearing if (we are picking k from a box K)
 and if random function take a parameter/seed timestamp*.
 Then better to try not to write message to start session in 
 same time. 
 in case K space is as big as 
 (miliseconds from birth to death of Alice and Bob)
 And they would take more than a milisecond to write a message
 And the mapping of timestamp to which memebers k is impossible 

 But then can't the eavsedropping party, be able to get same k
 by simulating the seed/timestamp, they know Alice sent the mssage
 at x time, then loop over random generator function to get K, which 
 would end up with subset of K, that might be practial to use 
 
 But anyway, probably modern random generator function, will take
 a)time, b) number of process working c) how busy is the CPU? 
 d) cpu temp ...etc to yet add more _thought to be random parameter_
 in picking `k`.

  In order to minize duplciate, one could though of stroing the used 
  key, but then it would solve something and create other probelem of 
  where/how to stroe used keys. And also alrgothim/software would be
  a new aspect of attaks, beacus it needs at somepoint to double check 
  if a picked key is already used...  

---end sidenote Q1---

** End of Question1 **

end of todo
--------
_Tries to answer what makes a cipher secured_

Check Shannon 1949, (it's why Dan called ciphers by Shannon) [Information theory] 

Conditions: 
 1. P(E(k,m0),c) = P (E(k,m1),c) i.e. the probablity of two messages m0,m1 (assume both 
 same length) is consistant. in other words if we know c, we cannot know anything about m, 
 or which m of the M of is most likely to be given c.
 We might have some lead as to what which m, but it's same lead for all memebers of M. 
 2. l(k) >= l(max(M)) which make it very unpractical e.g. for long message  
 3. otehr way to put given M(m0...mn) and C(c0,cn), taken cx at random, would have equal probabliity
 distrubuted among elemnts of M.
 4. **Need to revist**: > Key space K, has to be as large as M space 
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
  length of the key `k` is at least equal or greater than max length 
  `m` of the M space ~. Then `m xor k` will result c.   
  - But from practial point of view, we cannot send more messages than
  the maximum lenght of a message? since then k is not uniformely distrbuited?
   or k is resued again and also by necssiatity, we duplicate in `M`,
  thus elements of K, M, C are not uniformaly distrubuted 
  
- 
- For variable length time pad, it wouldn't work because the `c` length would 
  leak info about the length of the `m`.  
   - other way to put it, we would have some K that leads to a spesfic m, we don't
   need to guess total length of k. 
- practicaly aim for high Pc, and is perfect secureity isn't practical
- Change the key as frequent as could be (typically not starightforward or not in 
 hand of the end user) Adv
- Don't send same messge over and over again as it would minizie the unifromaity of space M
- It always assumed M and C are in spaces, probably for the easinesss of evacguons
- For whatever cipher is it, message max length shall has a relation with the frequency 
 of key rotation, and frequecy of key rotation if defined by `two weeks`...

## Ciphers
### 3.1 One-Time pad

Most straight forward form of encryption and is strong assuming is used only **once**.

The most important proetry is that size of `k` is equal to `m`. 

c = k ⊕ , m = k ⊕ c 

Note: the length of the key one time pad not necessarly same length as message
hence, is the cipher for perfect secuerty. 


