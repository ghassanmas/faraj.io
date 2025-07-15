

Python function to test theorem

```python
	def fl(p,a):
	"""
	- doesn't check if p is prime 
	- uses ** because of precison
	- returns true fermat little theorm  
	"""
		return ( ( (  ( p ** a ) - a ) % p ) == 0.0)
	
	
	def test_pl(p=7, r=100, verbose=False):
		sum_all = 0
		for i in range(0,r):
			result = fl(p,i)
			sum_all = int(result) + sum_all
	        if verbose:
		        print(f'little theorm with p is {p} and {i} is: {fl(p,i)}')
	    if(sum_all == r):
		    print(f"Sucess with p {p} and for {r} rounds")
		else:
			print(f"failed {(r - sum_all)} times with p {p} and for {r} rounds, Are you sure {p} is prime!?")
test_pl()
test_pl(6,33)
```