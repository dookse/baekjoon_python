from collections import Counter

c = Counter(list(input().upper()))
common1, *common2 = c.most_common()
if common2 and common1[1] == common2[0][1]:
    print('?')
else:
    print(common1[0])
