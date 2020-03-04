def func(confetti):
    M = len(confetti)
    minus = 0
    zero = 0
    one = 0
    for i in range(M):
        temp1 = 0 in confetti[i]
        temp2 = 1 in confetti[i]
        temp3 = -1 in confetti[i]
        if temp1 and not temp2 and not temp3:
            zero += 1
        elif temp2 and not temp1 and not temp3:
            one += 1
        elif temp3 and not temp1 and not temp2:
            minus += 1

    if zero == M: return 0, 1, 0
    if one == M: return 0, 0, 1
    if minus == M: return 1, 0, 0

    m, z, o = 0, 0, 0
    nexts = int(M/3)
    m_, z_, o_ = func([i[:nexts] for i in confetti[:nexts]])
    m += m_
    z += z_
    o += o_
    m_, z_, o_ = func([i[nexts:nexts*2] for i in confetti[:nexts]])
    m += m_
    z += z_
    o += o_
    m_, z_, o_ = func([i[nexts*2:] for i in confetti[:nexts]])
    m += m_
    z += z_
    o += o_
    m_, z_, o_ = func([i[:nexts] for i in confetti[nexts:nexts*2]])
    m += m_
    z += z_
    o += o_
    m_, z_, o_ = func([i[nexts:nexts*2] for i in confetti[nexts:nexts*2]])
    m += m_
    z += z_
    o += o_
    m_, z_, o_ = func([i[nexts*2:] for i in confetti[nexts:nexts*2]])
    m += m_
    z += z_
    o += o_
    m_, z_, o_ = func([i[:nexts] for i in confetti[nexts*2:]])
    m += m_
    z += z_
    o += o_
    m_, z_, o_ = func([i[nexts:nexts*2] for i in confetti[nexts*2:]])
    m += m_
    z += z_
    o += o_
    m_, z_, o_ = func([i[nexts*2:] for i in confetti[nexts*2:]])
    m += m_
    z += z_
    o += o_
    return m, z, o


N = int(input())

confetti = [[int(i) for i in input().split()] for _ in range(N)]
print(*func(confetti), sep='\n')