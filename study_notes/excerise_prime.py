
from is_prime import is_prime_dump



# Given prime numbers set S(n) [0,1,2,3,5,7] for n = 1 to N
# Create columns of P(x,y) where p(1,2) = s(1) * S(n) + S(2)
# P(1,3) = S(1) * S(n) + s(3)
# len( P(x,y) == N! )
# X,Y E (N)

# let's do for 

#Todo:
# the calcualted range shuld be used for drawings, instead of hard coding
# Refactor code

def draw_for_x_y(x=2, y=3, s=10, prime_only=True):
    """
    X: is the value to multilpy with 
    Y: is the value to add with
    S: is the range of n where n is: (0, 1, 2 ... S-1)
    prime_only: when true draw calculate value of n of S that
    is prime
    Given X,Y calcualte for range of S
    Note: when prime_only is true, it relfect the range, not the calculated
    value
    if it's prime X
    if it's not write it
    """
    # Calcualte range of S ...S-1, if prime only is True, filter the range for 
    #  prime numbers
    result = []
    range_s = [i for i in range(0,s) if (is_prime_dump(i) or not prime_only) ]
    max_digit_calc = len(str(((range_s[-1]) * x) + y))
    #max_digit_range = len(str(s-1))
    pad = 10 - max_digit_calc
    for i in range(0, s):
        if prime_only:
            if is_prime_dump(i):
                continue
        calc = (i * x) + y
        if (is_prime_dump(calc)):
            result.append("  " + f'\033[92m{calc}'.ljust(pad, ' ').rjust(2, ' '))
        else:
            result.append("  " + f'\033[91m{calc}'.ljust(pad, ' ').rjust(2, ' '))
    return result


def draw_for_x(x=2, s=10):
    result_2d = []
    # calculate
    for y in range(0, 10):
        result_2d.append(draw_for_x_y(x, y, s))
    # draw
    str_to_print = f'\033[95m (x,y)\\n| '
    for y in range(0, 10):
        str_to_print += f'\033[95m {y}  | '
    print(str_to_print)
    break_line = '-'*(s*5 + 15)
    print(break_line)

    for y in range(0, 10):
        str_to_print = "  " + f'\033[95m{x},{y}   |'
        range_ = len(result_2d[y])
        for y1 in range(0, range_):
            pad = 10 - len(str(result_2d[y][y1]))
            str_to_print+= f"{str(result_2d[y][y1]).ljust(pad, ' ')}"+"\033[95m|"
        print(str_to_print)





draw_for_x()
print("------------------------------break------------------------------")
draw_for_x(x=3)
print("------------------------------break------------------------------")
draw_for_x(x=5)
print("------------------------------break------------------------------")
draw_for_x(x=7)
print("------------------------------break------------------------------")
draw_for_x(x=9)
