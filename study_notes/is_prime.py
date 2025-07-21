import os, math


def is_prime_dump(p):
    sqrt_p = int(math.sqrt(p))
    range_chaek = sqrt_p + 1
    for i in range(2, range_chaek):
        if ((p % i) == 0):
            return False
    return True


def test_is_prime_dump():
    checks = []
    checks.append((is_prime_dump(3) == True))
    checks.append((is_prime_dump(4) == False))
    checks.append((is_prime_dump(17) == True))
    checks.append((is_prime_dump(10000) == False))
    checks.append((is_prime_dump(124141414146) == False))
    checks.append((is_prime_dump(29) == True))
    checks.append((is_prime_dump(37) == True))
    checks.append((is_prime_dump(61) == True))
    checks.append((is_prime_dump(77) == False))
    checks.append((is_prime_dump(19) == False))

    print(checks)


def print_prime_zero_two_hundered():
    for i in range(2,201):
        if (is_prime_dump(i)):
            print(f"{i} seems to be prime, oder?")
        
 
# test_is_prime_dump()
#print_prime_zero_two_hundered()
