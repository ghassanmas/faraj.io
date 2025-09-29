## The intersection with set and graph

The notions of outcomes is used through the set theory, a set becomes
an outcome space. 


TODO:
---------

On last note on indepeance. If we have three sets A, B, and C

As an axiom **A^B cannot be 0**, or in other world if both share no events
in common, then by definition, if A occured, there is higher priority event
B occuars OR it could be that **A and B are exclusive of each other**, which 
by common sense conflict with *knowing A doesn't reveal anything about B*, 

Another important point, is that, for A, B to be independt, it's by necessaity
knowing B, reveal nothing about A **OR** _reveal as much info relative to what
we don't know_ as we started.

Assuming event B depends on sequence of small events, while approaching B,
P(A), might have fluctuated, nonetheless, it setlled to same P(A) we started 
with as soon as B occured. AND it should to. 

Q: Followiong example on paper, get with expirmenet where |A^B| > 1 given 
the paper example was 1, and we know it cannot be 0. 

Paper example: 

Assuming we have box of balls of three colors are with equal distrubtion.
red, black, and yellow:

Expirment: we take 4 balls in sequence (i=1,2,3,4) For 3^4 times or 81

 **Assuming equal distribution of the 81**

Sets/Events are:  

 A { ball is red when i is even}    9/81 =  1/9
 B { ball is black when i is odd}   9/81 =  1/9 
 C { ball is green when i is even}  9/81 =  1/9

A^B = How many time of the 81, we get a sequence where it  {black, red
, black, red}, is 1= or 1/81 = 1/9 * 1/9 thus A and B are indepent.

Though when B occured, by neccesaity one of the 9 cases of _9/81 occured, 
but it's same ratio as 1/9_ e.g  `(8 / 72) = (1 / 9) = (9 /81)`  

Which sums it up as okay, we got one case of the A's but still we are left
left with same ratio. i.e the ( |A| / |Ω|)  is constant before and after
B occured. 

Note, in real life situation, it could be not that relastic if when |A|,
or |B| are in > 10^100000, magntinude. So _that B would occure without any 
noise of which would affect A_*, or might even be exculsive of it!.  

A and B would be still in theory indepenet, but how useful is that property
in real life, it depends on the cirumisatance of the expirmenet.                         

* Following in the book through the definition of **conditional indepence**p33-
p35, Given A and B are indepedent, this might not hold true if event C occured
and vise versa, in other words, if C is the noise, event A and B might no longer
be indepednet after C, or  if A and B are not indepedent, given C, A and B could
then be indepedent. See **Conditional Indepeance** below


______________________
Revisist defintion below, as A|B or A^B, if A are independent or are 
not. if A^B = 0 always are indepenent. Hence in Crypto book [^3]p11, we have 
       
  `Pr[m = m|c = c] = Pr[m = m].`  

**Independance**:        
       
          A,        if   A^B = AB       (Independent)
 A|B =
         A^B       
        -----,      if  A^B =/= AB     (Non-Indepednt)
          B

**Intersection**

                
           AB*,                if A|B = A (Independent)
   
 A^B =            -     -
          |Ω| - (|A| v |B|) , if A|B =/= A (Non-Indepedent)   
          -----------------
                |Ω|            
            |A|     |A^B|     |B|      |B^A|
*meaning: ------- = ----- OR ----- =  -------
            |Ω|    ||B|     ||Ω|     |A|    

 *This the a key distiguish between **Set Theory** and **Probability Theory**,
while the former _the world of sets_ as **static**, in the later things are in 
motion, or **dynamic**, or in set theory, we are concerned about counting the events
while in probability, we are concerned about the ratio of them. 



Example:
if we have a box balls, {A: 5 are red}, {B: are black},  


A: 5 red, B 5 black

If we put the balls all in box, and assume our expirment is that
we have to get two balls in sequenec: 

First ball
P(A) = 1/10 + 1/10 + 1/10 + 1/10 + 1/10 = 5/10 = 1/2 
P(B) = 1 - 1/2 = 1/2 (since we don't have other outcomes)

Second ball:
Well now, we already got one ball, and our expirment state 
so we are no longer with 5 ball for each color, thus we 
need to reconsider the ouctomes, and to branch

Second ball brnach1
P (A|B) if the first one was back

P(A|B) = 1/9 + 1/9 + 1/9 + 1/9 + 1/9 = 5/9
P(B|B) = 1 - 5/9 = 4/9

P(B) = Ω = 1/9 + 1/9 + 1/9 + 1/9 + 1/9 + 1/9 + 1/9 + 1/9 + 1/9 = 1 
 (see figure 2 below, if one of them x then,we are certian it's the outcome belong to B set)
A^B = P(B) - P(B|B) = P(A|B)

Second ball branch2
P(B|A) if the first one was red
P(A|A) = 1/9 + 1/9 + 1/9 + 1/9 = 4/9
P(B|A) = 1 - 4/9 = 5/9
 
P(B|A)

Conculusion: while A and B are _disjoint?_ list in this example
still were dependent, or **may be** not correct

Consider the following 3 figures

o: red ball
x: black ball
                                                ---------------------
------------------      --------------------    |     A         B    |
|   A       B    |      |    A       B      |   |   -----     -----  |
| ------  ------ |      |  --------------   |   |  | oo |    | xx |  |
| | o  |  | x  | |      |  | oo ' ox ' xx | |   |   -----     ----   |
| | oo |  | xx | |      |  |    ' xo '    | |   |   xo     ox        |
| | oo |  | xx | |      |  |--------------  |   |       Ω           |
| -----   -----  |      ---------------------   ---------------------
------------------            figure 2                   figure 3
     figure 1

One might image conceptlize the expirement, as figure 1, where A and B sepearte sets 
each with no overlapping elements A^B which is true to some exten, if per say our 
expirment state we need to get **only one ball**, however for figure 2 might better
represent the actual expirment or is more useful, since we have 4 outcomes and each 
of which 2 of them could have elemetns of A and B. while the third figure could useful
in case we only care about when the two balls are in the same color. 

Going back to same expirment, we showed how A and B are dependent, not because we 
have a ball that shares same color, rather because elements of A and B aren't 
uniformely distrbuted through the expirment. (since with the second we eneded up 
with less balls).



So how about if, we say after the first ball, before we get the second, 
we return the first to the box again. 

Assuming the first one was black

P(A|B) = 1/10 + 1/10 + 1/10 + 1/10 + 1/10 = 1/2 = P(A)
P(B|B) = P(B) (we still have 5 black balls)
 A^B = A.B (But note here P(B) alredy occured at this stage, so it's 1!)
    thus A^B = P(A) . 1  = P(A)
---------
END of Todo.


**Intersection**

The probablity of event A and B occured ~~at the sametime~~*, is the intersection 
so that `P(A)P(B)` = `A ∩ B` = `AB =  `A ^ B**`. 

 - From probabliity stand point AB is always less than or equal (A and B)
   - it would be equal only if any of (A, B) has probablity of 1, e.g. 
     it's space Ω

*sametime might not be correct word here, it needs revision see note todo above,
as the expirement condition play key role, e.g. _in terms of flipping the coin,
and predicting if head/tail, how many times the coin is exepcted to flip?_. 

**if A and B are **disjoint** list or independent

**Conditionility**

The probailty of an event A occurs **after** event occured, is so called conditionaility
and donated as `P(A|B)`; probability of A given B already occured.


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


**Conditional Indepeance**

Recall the definition above, two events A and B are independent
if P(A|B) = A, A^B = AB 

But what if we have another event called C, of which it might affect how A and B
are related if it occured.

P(A^B|C) = P(A|C) P(B|C) Then A,B are indepenet @ C 
  which is *irrelevant* to P(A|B) = B 

In other words, we could have a situation where once event C occuars, then the 
chance of A and B occuaring are equally likely but not necessarly if we have
event B occured, that A has same probablilty that we had in the begging.


An example: C is has no effect on A,B

Lets say we have space of numbers {i=1, i=20},

A = {i any odd numbers}
B = {i odd numbers, i>10}
C = {i, i>10, i<=20}

- Relation between A and B: 

P(A) = 10/20 = 1/2, 
P(B) = 5/20 = 1/4
A^B = 5/20 =1/4 but =/=  AB (Non Indepent)


- A and B with C 

Let's assume event C occured, meaning our space is now i>10,i<=20 

P(A|C) =  5/10 = 1/2 
 
P(B|C) = 5/10 = 1/2

P(A^B|C) = 5/10 =/= P(A|C)P(B|C) Thus still @ C, A and B and not independent
note that _B is is subset of A_

An example 2:  A and B are stil indendepent

A = {i, i%2==0}
B = {i, i%3==0}
C = {i, i%6==0} 
P(A) = 10/20 = 1/2 
P(B) = 6/20 = 3/10
A^B = 3 / 20 = AB (Thus A, and B are indepent)

How about @ C
A|C = 3/3 = 1 
B|C = 3/3 = 1 
P(A^B|C) = A|C * B|C (still independent?) 1*1 @ C we are certian A&B will occuar
note: _C is a subset of both A and B_


An example 3: A and B not indepent @ C
A {i, i%2==0}
B {i, i%3==0}
C {i, i%5==0}

A,B are independent (recall example 2 above)

However, @ C 
A|C = 2 / 4 = 1/2
B|C = 1 / 4  
P(A^B|C) = 0 =/= there can be no number between 1 and 20, that 
is divisable by 5, 3, and 2. 
In other words @ C A^B = 0, B and A became disjoint list @ C, which by 
definition cannot be true if A and B to be indepednet.  

_________________________________

For A and B to be indepedent:

- A must not be disjoint list of B 
- A and B cannot be a subset of each other?


Revisit _defination above after book also notes below_

 
 Which is irrelavnt to A and B indepeance in isolation to it.
  
 Note: if A is a subset of B, then no matter what is C, A and B 
 cannot be indepdent.     
 By defintion, if A is a subset of B are subset of each other:

 P(A|B) = 1 =/= AB
 P(B) > P(A) 
 P(A) < P(B) < 1 
 Thus P(A|B)  = 1 =/= 
 
@ C
 if C events didn't affect memeber of B thus A 
 P(A|C) < P(B|C) 


-------------------------------
Meta note:
 - the use of `^` instead of `∩` because it's used elsewhere, and easier to type!


-------------------------------

Refrences: 

- [book] Bertsekas Tsitsiklis Introduction to Probability
- [LLM] https://chatgpt.com/share/68d3e5e3-9a50-8004-976d-3cf17995e07c 
