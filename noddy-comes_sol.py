
def get_route(c_map, n, m,rt):
    rt = rt+c_map[0]
    if n == 1:
        return rt
    if m == 1:
        for v in range(1, n):
            rt.append(c_map[v][0])
        return rt


    rt = rt+[val[-1] for val in c_map[1:]]
    t = c_map[-1][0:-1]
    t.reverse()
    rt = rt+t
    t = [val[0] for val in c_map[1:-1]]
    t.reverse()
    rt = rt+t
    if n == 2 or m == 2:
        return rt
    n_map = [[None]*(m-2)]*(n-2)
    for i in range(n-2):
        n_map[i] = c_map[i+1][1:-1]

    return get_route(n_map, n-2, m-2,rt)


if __name__ == "__main__":
    l1 = input().strip()
    n,m =l1.split(" ")
    n, m = int(n), int(m)
    mat = [[None] * m] * n
    for i in range(n):
        t = input().strip()
        tw = t.split(" ")
        mat[i] = [int(k) for k in tw]
    k = int(input().strip())

    route=get_route(mat, n, m, [])
    if k >= len(route):
        k = k % len(route)
        res = route[k:] + route[0:k]
    elif k == len(route):
        res = route
    else:
        res=route[k:]+route[0:k]

    for val in res:
        print(val, end=" ")



