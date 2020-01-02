size = int(input())
inputs = list(map(int, input().split()))
inputs.sort()
print('{} {}'.format(inputs[0], inputs[size - 1]))
