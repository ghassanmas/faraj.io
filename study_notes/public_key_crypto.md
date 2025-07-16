
Is public key a protocol


## History of development
### Merkle

Note: technically it might not be a public, because the shared token cannot be known to public. which in the example below is `puzzle`.  

 it works first, that the parties agrees on a shared token "puzzle" among them. 
- Alice would for 2^32 times encrypt the message:  `E(p) = ( pi [K] , [M] (puzzle  {xi} || {ki})`
- Bob choose one of them e.g. E(123) 
	- Loop over 2^32 trying and calculate D(123)  times where `M` of `D(123)` = or starts with `puzzle`  . i.e. what is value of `P` that satisfies D(123)
	- Sends X(123) to Alice
- Alice knows K(123) is to be used key 
- Eavesdropper since dosen't know `M` has to start with `Puzzle` they have to 
	- Go over all E(p) 2^23
		- and for each E(p) go over all values of  P 2^32
			- Find which one has X(j) 

### Diffe-Hillman 

### RSA 


## Expirmenting

#### checking for RSA prime numbers

To check if a number is really prime, an algorthim has O(n) of at least (2**1024). If we choose to not to rely in probablity, then we might not choose a prime number, e.g. instead of trusting the number is really prime, we are trusting whatever claim is it that the number if prime. 

#### Steps to check

- Generate key pair, and check if their prime is really prime 
	- It should be checked for at least N (what is value for N so it's trust worthy?)
	

Time to check relate to number of digit running python3.12 on Mac apple silicon 2019


| digit # | time (seconds)       |
| ------- | -------------------- |
| 8       | 0.42(max) 0.25(min)  |
| 9       | 4.03(max) 2.5(min)   |
| 10      | 38.22(max) 26.1(min) |
| 11      | ~400()????           |
|         |                      |

#### checking eliptic curve 

- 





The goal to check the integrity of the offline tool to generate key pair. 

Summarize how the private public keys is generated. 
- e.g. generate 100s key pairs with gpg check if prime 
- what does 2048 bit translate to the size of prime number
- When an algorthim generate prime number, does it really check if it's prime or it's probalistic 


Todo: 
- Generate RSA 