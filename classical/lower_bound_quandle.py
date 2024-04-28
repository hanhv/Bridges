import pandas as pd
from sympy import *


def use_favorite_quandle(gauss_code, quandle):
    my_gauss2pd = gauss2pd([gauss_code])
    my_pdhomlist = pdhomlist(my_gauss2pd, quandle)
    my_length = len(my_pdhomlist)
    return my_length


###########################
# Planar Diagram stuff
###########################


def pdhomlist(PD, N):  # list quandle homomorphisms
    ###Lists homomorphisms from knot rack/quandle of planar diagram###
    z = []
    for i in range(1, 2 * len(PD) + 1):
        z = z + [0]
    L = [z]
    out = []
    while len(L) != 0:
        w = L[0]
        L[0:1] = []
        if w:
            i = hfindzero(w)
            if not i:
                out.append(w)
            else:
                for j in range(1, len(N) + 1):
                    phi = list(w)
                    phi[i - 1] = j
                    v = pdhomfill(PD, N, phi)
                    if v: L.append(tuple(v))
    return out


def hfindzero(f):
    ### find zero in homomorphism template ###
    j = -1
    for i in range(0, len(f)):
        if f[i] == 0:
            j = i + 1
            break
    if j < 0:
        out = False
    else:
        out = j
    return out


def pdhomfill(PD, N, phi):  # fill in homomorphism
    ###Fills in entries in a homomorphism###
    f = phi
    c = True
    out = True
    while c == True:
        c = False
        for X in PD:
            if f[X[2] - 1] == 0 and f[X[4] - 1] != 0:
                f[X[2] - 1] = f[X[4] - 1]
                c = True
            if f[X[4] - 1] == 0 and f[X[2] - 1] != 0:
                f[X[4] - 1] = f[X[2] - 1]
                c = True
            if f[X[4] - 1] != f[X[2] - 1] and (f[X[2] - 1] != 0 and f[X[4] - 1] != 0):
                out = False
            if X[0] == 1:
                if f[X[1] - 1] != 0 and f[X[4] - 1] != 0:
                    if f[X[3] - 1] == 0:
                        f[X[3] - 1] = N[f[X[1] - 1] - 1][f[X[4] - 1] - 1]
                        c = True
                    elif f[X[3] - 1] != N[f[X[1] - 1] - 1][f[X[4] - 1] - 1]:
                        out = False
            if X[0] == -1:
                if f[X[3] - 1] != 0 and f[X[4] - 1] != 0:
                    if f[X[1] - 1] == 0:
                        f[X[1] - 1] = N[f[X[3] - 1] - 1][f[X[4] - 1] - 1]
                        c = True
                    elif f[X[1] - 1] != N[f[X[3] - 1] - 1][f[X[4] - 1] - 1]:
                        out = False
    if out == True:
        return f
    else:
        return out


def gauss2pd(G):
    ###convert Gauss code to planar diagram###
    out = []
    semiarccount = 0
    complen = []
    for i in range(0, len(G)):
        semiarccount = semiarccount + len(G[i])
        complen.append(len(G[i]))
    nx, cr = [], []
    for k in range(0, semiarccount):
        nx.append(0)
        cr.append(0)
    current = 1
    i = 0
    for x in range(1, len(G) + 1):
        for y in range(1, len(G[x - 1]) + 1):
            i = i + 1
            if y == complen[x - 1]:
                nx[i - 1] = current
            else:
                nx[i - 1] = i + 1
            j = 0
            for z in range(1, len(G) + 1):
                for w in range(1, len(G[z - 1]) + 1):
                    j = j + 1
                    if G[z - 1][w - 1] + G[x - 1][y - 1] == 0:
                        cr[i - 1] = j
        current = current + complen[x - 1]
    i = 0
    for x in range(1, len(G) + 1):
        for y in range(1, len(G[x - 1]) + 1):
            i = i + 1
            if G[x - 1][y - 1] < 0:
                if G[x - 1][y - 1] % 1 == 0:
                    out.append([1, i, nx[cr[i - 1] - 1], nx[i - 1], cr[i - 1]])
                else:
                    out.append([-1, i, cr[i - 1], nx[i - 1], nx[cr[i - 1] - 1]])
    return out


# BE VERY CAREFUL: THERE ARE count and count1
def gbbrcount1(g, M):
    ### blackboard birack counting polynomial ###
    N = birackrank(M)
    q = Symbol('q')
    x = Symbol('x')
    x = 0
    w = g
    for n in range(0, N):
        x = x + len(biqpdhomlist(gauss2pd(w), M)) * q ** (gausswrithe(w[0]) % N)
        w = gaussinc(w, 1)
    return x


def gaussbbrcount2(G, T):
    ### Gauss code birack counting invariant###
    comp = len(G)
    N = birackrank(T)
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    x = Symbol('x')
    x = 0
    w = G
    for i in range(0, N):
        for j in range(0, N):
            x = x + len(biqpdhomlist(gauss2pd(w), T)) * q1 ** (gausswrithe(w[0]) % N) * q2 ** (gausswrithe(w[1]) % N)
            w = gaussinc(w, 2)
        w = gaussinc(w, 1)
    return x


def gaussbbrcount3(G, T):
    ###Gauss code birack counting invariant###
    comp = len(G)
    N = birackrank(T)
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    q3 = Symbol('q3')
    x = Symbol('x')
    x = 0
    w = G
    for i in range(0, N):
        for j in range(0, N):
            for k in range(0, N):
                x = x + len(biqpdhomlist(gauss2pd(w), T)) * q1 ** (gausswrithe(w[0]) % N) * q2 ** (
                        gausswrithe(w[1]) % N) * q3 ** (gausswrithe(w[2]) % N)
                w = gaussinc(w, 3)
            w = gaussinc(w, 2)
        w = gaussinc(w, 1)
    return x


def gaussbbrcount4(G, T):
    ###Gauss code rack counting invariant###
    comp = len(G)
    N = birackrank(T)
    q1 = Symbol('q1')
    q2 = Symbol('q2')
    q3 = Symbol('q3')
    q4 = Symbol('q4')
    x = Symbol('x')
    x = 0
    w = G
    for i in range(0, N):
        for j in range(0, N):
            for k in range(0, N):
                for l in range(0, N):
                    x = x + len(biqpdhomlist(gauss2pd(w), T)) * q1 ** (gausswrithe(w[0]) % N) * q2 ** (
                            gausswrithe(w[1]) % N) * q3 ** (gausswrithe(w[2]) % N) * q4 ** (gausswrithe(w[3]) % N)
                    w = gaussinc(w, 4)
                w = gaussinc(w, 3)
            w = gaussinc(w, 2)
        w = gaussinc(w, 1)
    return x


def gbbrcount(G, T):
    ###Gauss code birack counting invariant###
    n = len(G)
    if n == 1:
        out = gbbrcount1(G, T)
    elif n == 2:
        out = gaussbbrcount2(G, T)
    elif n == 3:
        out = gaussbbrcount3(G, T)
    elif n == 4:
        out = gaussbbrcount4(G, T)
    return out


def gausswrithe(g):
    ###self-crossing sum of component###
    out = 0
    for i in range(0, len(g)):
        if g[i] < 0:
            for j in range(0, len(g)):
                if g[i] + g[j] == 0:
                    if type(g[i]) == int:
                        out = out + 1
                    if type(g[i]) == float:
                        out = out - 1
    return out


def biqpdhomlist(PD, N):
    ###Lists homomorphisms from knot biquandle/birack of planar diagram###
    z = []
    for i in range(1, 2 * len(PD) + 1):
        z = z + [0]
    L = [z]
    out = []
    while len(L) != 0:
        w = L[0]
        L[0:1] = []
        if w:
            i = hfindzero(w)
            if not i:
                out.append(w)
            else:
                for j in range(1, len(N[0]) + 1):
                    phi = list(w)
                    phi[i - 1] = j
                    v = biqpdhomfill(PD, N, phi)
                    if v: L.append(tuple(v))
    return out


def biqpdhomfill(PD, N, phi):  # fill in homomorphism
    ###Fills in entries in a biquandle homomorphism###
    U, L = N[0], N[1]
    Nb = barops(N)
    Ub, Lb = (Nb[0], Nb[1])
    f = phi
    c = True
    out = True
    while c == True:
        c = False
        for X in PD:
            if X[0] == 1:
                if f[X[1] - 1] != 0 and f[X[4] - 1] != 0:
                    if f[X[3] - 1] == 0:
                        f[X[3] - 1] = U[f[X[1] - 1] - 1][f[X[4] - 1] - 1]
                        c = True
                    if f[X[3] - 1] != U[f[X[1] - 1] - 1][f[X[4] - 1] - 1]:
                        return False
                    if f[X[2] - 1] == 0:
                        f[X[2] - 1] = L[f[X[4] - 1] - 1][f[X[1] - 1] - 1]
                        c = True
                    if f[X[2] - 1] != L[f[X[4] - 1] - 1][f[X[1] - 1] - 1]:
                        return False
            if X[0] == -1:
                if f[X[1] - 1] != 0 and f[X[2] - 1] != 0:
                    if f[X[3] - 1] == 0:
                        f[X[3] - 1] = Ub[f[X[1] - 1] - 1][f[X[2] - 1] - 1]
                        c = True
                    if f[X[3] - 1] != Ub[f[X[1] - 1] - 1][f[X[2] - 1] - 1]:
                        return False
                    if f[X[4] - 1] == 0:
                        f[X[4] - 1] = Lb[f[X[2] - 1] - 1][f[X[1] - 1] - 1]
                        c = True
                    if f[X[4] - 1] != Lb[f[X[2] - 1] - 1][f[X[1] - 1] - 1]:
                        return False
    return f


def barops(M):
    ###get barred ops from birack matrix###
    U, L, n = M[0], M[1], len(M[0])
    Ub, Lb = zeromatrix(n), zeromatrix(n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            Ub[U[i - 1][j - 1] - 1][L[j - 1][i - 1] - 1] = i
            Lb[L[j - 1][i - 1] - 1][U[i - 1][j - 1] - 1] = j
    return (Ub, Lb)


def gaussinc(G, c):
    ###increment writhe in component c###
    M = 0
    for x in G:
        M = M + len(x)
    j = M / 2 + 1
    out = []
    count = 0
    for x in G:
        if count == c - 1:
            out.append(x + [-j, j])
        else:
            out.append(x)
        count = count + 1
    return out


def birackrank(M):
    ###find birack rank ###
    return permorder(pi(M))


def pi(M):
    ### type I move bijection positive twist ###
    D = diagonalmaps(M)
    return permcomp(perminv(D[0]), D[1])


def diagonalmaps(M):
    ### get diagonal bijections; return False else ###
    S = sideops(M)
    S1, S2, n = S[0], S[1], len(S[0])
    x, y = [], []
    for i in range(1, n + 1):
        x.append(S1[i - 1][i - 1])
        y.append(S2[i - 1][i - 1])
    if reptest(x) and reptest(y):
        return [x, y]
    return False


def reptest(p):  # test whether p has repeated non-zero entries
    ###Test whether p has repeated non-zero entries###
    q = True
    L = []
    for i in range(1, len(p) + 1):
        if p[i - 1] != 0:
            if p[i - 1] in L:
                q = False
            else:
                L.append(p[i - 1])
    return q


def sideops(M):
    ### get sideways operations from birack matrix ###
    U, L = M[0], M[1]
    n = len(U)
    S1, S2 = zeromatrix(n), zeromatrix(n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            S1[i - 1][L[j - 1][i - 1] - 1] = j
            S2[i - 1][L[j - 1][i - 1] - 1] = U[i - 1][j - 1]
    if findzero(S1) or findzero(S2):
        return False
    return ([S1, S2])


def findzero(M):
    ### Find position of first zero entry in a matrix ###
    out = False
    for i in range(1, len(M) + 1):
        if not out:
            for j in range(1, len(M[0]) + 1):
                if M[i - 1][j - 1] == 0:
                    out = (i, j)
                    break
    return out


def zeromatrix(n):
    ### return n by n zero matrix###
    out = []
    for i in range(0, n):
        r = []
        for j in range(0, n): r.append(0)
        out.append(r)
    return out


#######################################
# Biquandles and biracks
#######################################

def perminv(v):
    ###inverse of a permutation###
    out = []
    for i in range(1, len(v) + 1):
        out.append(0)
    for i in range(1, len(v) + 1):
        out[v[i - 1] - 1] = i
    return out


def permorder(p):
    ### order of a permutation p###
    i = 1
    x = list(p)
    id = []
    for j in range(1, len(p) + 1):
        id.append(j)
    while x != id:
        x = list(permcomp(x, p))
        i = i + 1
    return i


def permcomp(p, q):
    ### Compose permutations###
    out = []
    for i in range(1, len(p) + 1):
        out.append(q[p[i - 1] - 1])
    return tuple(out)
