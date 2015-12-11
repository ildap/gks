from method import Gauss

def compute(y):
    x = range(0,len(y))
    m1 = sum([i*i for i in x])
    m2 = sum(x)
    n1 = m2
    n2 = len(x)
    c1 = 0
    c2 = sum(y)
    for i in range(0, len(x)):
        c1 += x[i] * y[i]

    G = Gauss([[m1, n1, c1],
               [m2, n2, c2]], True)
    print 'a = ', G[0], ' b = ', G[1]
    print 'f(x) = {}*x + {}'.format(G[0], G[1])
    return G
