from math import comb

one_m_cnt = 0
for i in range(23, 101):
    for j in range(1, i+1):
        combinations = comb(i, j)
        # print(i, j, combinations)
        if combinations > 1000000:
            one_m_cnt += 1

print(one_m_cnt)