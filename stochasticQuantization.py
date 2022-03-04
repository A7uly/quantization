import math
import random

def stochasticQuantization(x, q, p):
    # x = local model of user i
    # q = quantization level
    # p = modulo p

    # var_x = quantized x
    var_x = mappingX(q * stochasticRounding(x, q), p)
    return var_x

def stochasticRounding(x, q):
    # x = local model of user i
    # q = quantization level

    # ret_list = return value list after rounding x
    # prob_list = probability list (weight for random.choices)
    # ret_x = rounded x

    ret_list = [math.floor(q * x) / q, (math.floor(q * x) + 1) / q]
    prob_list = [1 - (q * x - math.floor(q * x)), q * x - math.floor(q * x)]
    ret_x = random.choices(ret_list, prob_list)
    return ret_x

def mappingX(x, p):
    """mappingX(x, p) is to represent a negative integer in the finite field
    by using two’s complement representation"""
    # % mod 연산으로 대체가 가능한 부분인가...?
    if x < 0:
        return p + x
    else:
        return x
