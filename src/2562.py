input_list = []
for i in range(9):
    input_list.append(input())
max_value = max(input_list)
print(max_value)
print((input_list.index(max_value) + 1))
