## The intersection with set and graph

The notions of outcomes is used through the set theory, a set becomes
an outcome space. 


**Intersection**

The probablity of event A and B occured **at the sametime**, is the intersection 
so that `P(A)P(B)` = `A ∩ B` = `AB =  `A ^ B`. 

 - From probabliity stand point AB is always less than or equal (A and B)
   - it would be equal only if any of (A, B) has probablity of 1, e.g. 
     it's space Ω

**Conditionility**

The probailty of an event A occurs **after** event occured, is so called intersection
so that `P(A|B)`


Let's assume we already have an event that is in set of B occured, 
what is the probability, that that elemnt of B, is also part of the 
intersection of them. 

Let's assume, B is a subset of A, then it's has definilty occured. 
and the result suppose to be 1.

Let's assume, none of element of B exists in A, then the result 
suppose to be 0. 

So the probablity event A occurs depends on how many of the element in
B, are or are not part of the intersection of A and B. 

             A ^ B           Note if B is a subset of A, then A^B = B
 P(A|B) =  ---------
              B


Note: from presentage (0..1), A^B is always smaller or equal than A,B
however for A|B, we might end with > B, because from a common sense B
already occured, so we don't need to condition it. While for A^B, 
it cannot be bigger than both of them. 

Other way to put it, is that for A^B our space of refrence Ω,however for 
A|B, our space of refrence becomes B. hence B already occured while in 
the former Ω always contains all possible scinarios  


-------------------------------

with Graph Theory 

So far we used set and probability interchargerbaly, one clear usage of graph for [^1]p8, 
is that when doing expirmenets in space Ω, if it's important to note thesequences 
of the outcomes. Then the sequences is translated to path. 

In other words, counting path with length n larger than > is the space of A.


-------------------------------
Meta note:
 - the use of `^` instead of `∩` because it's used elsewhere, and easier to type!


-------------------------------

Refrences: 

- [book] Bertsekas Tsitsiklis Introduction to Probability
- [LLM] https://chatgpt.com/share/68d3e5e3-9a50-8004-976d-3cf17995e07c 
