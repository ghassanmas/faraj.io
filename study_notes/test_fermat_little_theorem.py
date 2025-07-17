"""
This module test fermat little theorem

Note: the result of expirement, is as trust worthy, as source
code of python. e.g. if there is a malfuction if Ptyhon source
code it would be reflect on this.

"""


def fl(p, a):
    """
        - doesn't check if p is prime
        - uses ** because of precison
        - returns true fermat little theorm
    """
    return ((((a ** p) - a) % p) == 0.0)


def test_pl(p=7, r=10000, verbose=False):
    sum_all = 0
    for i in range(0, r):
        result = fl(p, i)
        sum_all = int(result) + sum_all
        if verbose:
            print(f'little theorm with p is {p} and {i} is: {fl(p, i)}')
    if (sum_all == r):
        print(f"Sucess for p = {p} and for a in range  (0, ... {r})")
    else:
        print(
            f"""failed {(r - sum_all)} times with p {p} and for a in range
             (0, ... {r}),Are you sure {p} is prime!?""")


print("test little theorem with random number migh or might be prime")
"""
for j in ([3, 7, 13, 15, 59, 73, 77, 1991, 1044388881413152506691752710716624382579964249047383780384233483283953907971557456848826811934997558340890106714439262837987573438185793607263236087851365277945956976543709998340361590134383718314428070011855946226376318839397712745672334684344586617496807908705803704071284048740118609114467977783598029006686938976881787785946905630190260940599579453432823469303026696443059025015972399867714215541693835559885291486318237914434496734087811872639496475100189041349008417061675093668333850551032972088269550769983616369411933015213796825837188091833656751221318492846368125550225998300412344784862595674492194617023806505913245610825731835380087608622102834270197698202313169017678006675195485079921636419370285375124784014907159135459982790513399611551794271106831134090584272884279791554849782954323534517065223269061394905987693002122963395687782878948440616007412945674919823050571642377154816321380631045902916136926708342856440730447899971901781465763473223850267253059899795996090799469201774624817718449867455659250178329070473119433165550807568221846571746373296884912819520317457002440926616910874148385078411929804522981857338977648103126085903001302413467189726673216491511131602920781738033436090243804708340403154190336]):
    test_pl(j)
"""

# how long it takes to calculate if ~300 digit number to find it's really true


def how_long_to_take(p=2**1024):
    import time
    time_now = time.time()
    print(f"time now is {time_now}, start to check for {p}")
    number_to_check = int(p / 2)
    failed = 0
    for i in range(2, number_to_check):
        if ((p % i) != 0):
            failed += 1  # This just dump opreation we will keep rotating
    diff_time = time.time() - time_now
    print(
        f"the time to really check if {p} is really prime, took {diff_time} seconds")


def how_long_to_take_no_write(p=2**1024):
    import time
    time_now = time.time()
    print(f"time now is {time_now}, start to check for {p}")
    number_to_check = int(p / 2)
    for i in range(2, number_to_check):
        if ((p % i) != 0):
            continue  # nothing, noneed to write to memorey
    diff_time = time.time() - time_now
    print(
        f"the time to really check if {p} is really prime, took {diff_time} seconds")


"""
for j in [7, 22, 444, 5555, 66666, 2**1024]:
    how_long_to_take(j)
"""
# Let's calculate 7 digits
# with no momrey write
how_long_to_take_no_write(1000000)


# Let's calculate 8 digits
# with no momrey write
how_long_to_take_no_write(10000000)


# Let's calculate 9 digits
# with no momrey write
how_long_to_take_no_write(100000000)


# Let's calculate 10 digits
# with no momrey write
how_long_to_take_no_write(1000000000)


# Let's calculate 11 digits
# with no momrey write
how_long_to_take_no_write(10000000000)


# dump check, let see how long it take in time as number digits
# yes it's dump as expectred, it suppose to be sqrt(p)
# secondaly, we can optimize by checking factorinzing 
# of the prime numbers (1...n-1), where n is sqrt(p) 
# increase, 1, 2, 3, 4 digit
# Let's calucalte from 1 to 100 digits
for i in range(1, 100):
    p_check = int('1' + ('0' * i))
    print(f"running for {p_check} digits")
    how_long_to_take(p_check)
