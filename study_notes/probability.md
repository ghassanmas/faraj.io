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
but it's same ratio as 1/9_ e.g  `8 / 72 = 1 / 9 = 9 /82`  

Which sums it up as okay, we got one case of the A's but still we are left
left with same ratio of A complement. 
                        
______________________
Revisist defintion below, as A|B or A^B, if A are independent or are 
not. if A^B = 0 always are indepenent. Hence in Crypto book [^3]p11, we have 
       
  `Pr[m = m|c = c] = Pr[m = m].`  

**Conditionatlily**:        
        

       if      A^B = 0?,     A*       (Independent)
 A|B =
                            A^B       
       if     A^B =/= 0,   -----     (Non-Indepednt)
                             B
**Intersection**
 
       if   A|B = A,             (Independent)
                             A.B   (in case A, B are disjoint partition of omega, and A|B =A
                                    and be is B is 1, thus A|B = A^B = A
 A^B                =            --      --
                         |Ω|-   |A |  v  B| ??????????????? (Need revision)
      if   A|B =/= A,   ----------------------    (non-Indepenedt)
                                |Ω|
 ?it could be 0 from set theory presepective but not necessary indepedent 

 *This the a key distiguish between **Set Theory** and **Probability Theory**,
while the former _the world of sets_ as **static**, in the later things are in 
motion, or **dynamic**, in other wors if a box balls, {A: 5 are red}, {B: are black},  


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


-------------------------------
Meta note:
 - the use of `^` instead of `∩` because it's used elsewhere, and easier to type!


-------------------------------

Refrences: 

- [book] Bertsekas Tsitsiklis Introduction to Probability
- [LLM] https://chatgpt.com/share/68d3e5e3-9a50-8004-976d-3cf17995e07c 
