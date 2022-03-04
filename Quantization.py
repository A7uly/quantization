import math
import random

def SS_Matrix(G):
    # G = the number of groups
    B = [['*' for x in range(G)] for y in range(G)]
    for g in range(G - 1):
        for r in range(G - g - 1):
            l = 2 * g + r
            B[l % G][g] = g
            B[l % G][g + r + 1] = g
    for i in range(G):
        for j in range(G):
            if B[i][j] == '*':
                B[i][j] = j
    return B

# generate G quantizers randomly
def generateQuantizers_heteroQ(G):
    Q = []
    for i in range(G):
        Q.append(random.randint(1, 100))
    return Q

# return quantization level q
def returnQuantizer(mode, l, g, B, Q):
    # mode = homo quantization(0) or hetero quantization(1)
    # l = segment index
    # g = group index
    # B = SS_Matrix
    # Q = a set of quantization level

    # q = quantization level
    if mode == 0:  # homo quantization
        q = Q[0]
        return q
    elif mode == 1:  # hetero quantization
        q = Q[B[l][g]]
        return q
    else:
        print("wrong input")
        return 0

def Quantization(x, G, q, r1, r2):
    # x = local model value of user i
    # G = the number of groups
    # q = quantization level
    # [r1, r2] = quantization range
    """ q = returnQuantizer(mode, l, g, B, Q)
    => Quantization(x, G, q) can do both homo quantization and hetero quantization. """

    # delK = quantization interval
    # T = discrete value from quantization range point list
    delK = (r2 - r1) / (q - 1)
    T = []
    for l in range(0, G):
        T.append(r1 + l * delK)

    for l in range(0, G - 1):
        if T[l] <= x < T[l + 1]:
            ret_list = [T[l], T[l+1]]
            prob_list = [(x - T[l]) / (T[l + 1] - T[l]), 1-((x - T[l]) / (T[l + 1] - T[l]))]
            ret_x = random.choices(ret_list, prob_list)
            break
    return ret_x
