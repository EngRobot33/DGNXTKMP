def first(inp: str, n: int):
    quotient, remainder = divmod(n, len(inp))
    return (inp*quotient + inp[:remainder]).count('a')


def second(inp: str):
    counter = 0
    for i in range(len(inp) - 1):
        if inp[i] == inp[i + 1]:
            counter += 1
    return counter


def third(inp: list):
    n = len(inp)
    pos = [*enumerate(inp)]
    pos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}

    res = 0
    for i in range(n):
        if vis[i] or pos[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not vis[j]:
            vis[j] = True
            j = pos[j][0]
            cycle_size += 1

        if cycle_size > 0:
            res += (cycle_size - 1)
    return res
