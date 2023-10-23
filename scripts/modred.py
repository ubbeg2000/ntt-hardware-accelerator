from random import randint

m = 16
M = int(2**16)
Q = M + 1

for a in [(M+M)*65471]:
    t = a % M - (a >> m)
    # if t > Q:
    # print(a, t)
    if t >= 0 and t < Q:
        print(t, a % Q, t == a % Q)
    elif t <= -Q:
        print(t + 2*Q, a % Q, t + 2*Q == a % Q)
    elif t >= Q:
        print(t - Q, a % Q, t - Q == a % Q)
    else:
        print(t + Q, a % Q, t + Q == a % Q)

    # t = t % M - (t >> m)  
    # if t >= 0 and t < Q:
    #     print(t, a % Q, t == a % Q)
    # elif t >= Q:
    #     print(t - Q, a % Q, t - Q == a % Q)
    # else:
    #     print(t + Q, a % Q, t + Q == a % Q)

print(max([(pow(3, -2*i, Q) * (pow(2, -1, Q))) % Q for i in range(1023)]))