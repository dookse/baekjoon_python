t = int(input())
for tt in range(t):
    line = input()
    pre_score, total_score = 0, 0
    for c in line:
        if c == 'O':
            pre_score += 1
        else:
            pre_score = 0
        total_score += pre_score
    print(total_score)
