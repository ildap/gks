def Gauss(m,p):
    # eliminate columns

    if p:
        for sm in m:
            print(sm)
        print()
    for col in range(len(m[0])):
        for row in range(col + 1, len(m)):

            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
            if p:
                for sm in m:
                    print(sm)
                print()

    # now backsolve by substitution
    ans = []
    # makes it easier to backsolve
    m.reverse()
    for sol in range(len(m)):
        if sol == 0:
            ans.append(m[sol][-1] / m[sol][-2])
        else:
            inner = 0
            # substitute in all known coefficients
            for x in range(sol):
                inner += (ans[x] * m[sol][-2 - x])
            # the equation is now reduced to ax + b = c form
            # solve with (c - b) / a
            ans.append((m[sol][-1] - inner) / m[sol][-sol - 2])
    ans.reverse()


    return ans


def test():
    print(Gauss([[3, 2, 1, 5],
                 [1, 1, -1, 0],
                 [4, -1, 5, 3]]),
          '"-1,3,2"')

