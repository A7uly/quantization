import math
import random
# import numpy as np

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


def homo_q(x_i, G, N):
    vx_i = []
    T = []  # discrete value from quantization range
    r1, r2 = 0, 100  # quantization range
    q = random.randint(1, 100)  # quantization level
    delK = (r2 - r1) / (q - 1)  # quantization interval
    for l in range(0, q):
        T.append(r1 + l * q)
    for i in x_i:
        for l in range(0, q-1):
            if T[l] <= i < T[l + 1]:
                prob = (i - T[l]) / (T[l+1] - T[l])
                if prob < 0.5:
                    vx_i.append(T[l])
                else:
                    vx_i.append(T[l+1])

def hetero_q(x_i, G, N):
    vx_i = []
    T = []
    r1, r2 = 0, 100
    B = SS_Matrix(G)
    q = generateQuantizers_heteroQ(G)
    delK = (r2 - r1)/ (q - 1)
    for l in range(0, q):
        T.append(r1 + l * q)
    for i in x_i:
        for l in range(0, q-1):
            if T[l] <= i < T[l + 1]:
                prob = (i - T[l]) / (T[l+1] - T[l])
                if prob < 0.5:
                    vx_i.append(T[l])
                else:
                    vx_i.append(T[l+1])


def generateQuantizers_heteroQ(G):
    Q = []  # generate G quantizers randomly
    for i in range(G):
        Q.append(random.randint(1, 100))
    return Q

# set quantization level q
def setQuantizer(G, mode, l, g, B):
    # G = the number of groups
    # mode = homo quantization(0) or hetero quantization(1)
    # l = segment index
    # g = group index

    if mode == 0:  # homo quantization
        q = random.randint(1, 100)  # quantization level
        return q
    elif mode == 1:  # hetero quantization
        Q = generateQuantizers_heteroQ(G) # a set of quantization level
        q = Q[B[l][g]]
        return q
    else:
        print("wrong input")
        return 0

def homoQ(x, q):
    """x = local model value of user i
    q = setQuantizer(G, mode, l, g, B) = quantization level
    => can do both homo quantization and hetero quantization"""

    r1, r2 = 0, 100  # quantization range
    delK = (r2 - r1) / (q - 1)  # quantization interval
    T = []  # discrete value from quantization range
    for l in range(0, q):
        T.append(r1 + l * q)

    for l in range(0, q - 1):
        if T[l] <= x < T[l + 1]:
            prob = (x - T[l]) / (T[l + 1] - T[l])
            if prob < 0.5:
                return T[l]
            else:
                return T[l+1]





