import math
import random
# import numpy as np

def stochastic_q(w_i): # w_i = local model of user i
    vx_i = []
    q = random.randint(1, 100)  # quantization level
    p = random.randint(1, 100)  # modulo p
    for x in w_i:
        vx_i.append(pi_x(q * qq_x(x, q), p))
    return vx_i

def qq_x(x, q):
    prob = q * x - math.floor(q * x)
    if prob < 0.5:
        return math.floor(q * x) / q
    else:
        return (math.floor(q * x) + 1) / q

"""pi_x(x) is to represent a negative integer in the finite field
by using two’s complement representation"""

def pi_x(x, p):
    # % mod 연산으로 대체가 가능한가...?
    if x < 0:
        return p + x
    else:
        return x