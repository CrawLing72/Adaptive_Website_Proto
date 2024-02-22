total_list = []

count = int(1e9)
i_main = 0

for _ in range(N):
    total_list.append([int(x) for x in sys.stdin.readline().rstrip().split()])

for i in range(257):
    installed_num = 0
    removed_num = 0

    for x in range(M):
        for y in range(N):
            det = total_list[y][x] - i
            if det > 0:
                removed_num += det
            else:
                installed_num -= det

    if B + removed_num < installed_num:
        continue
    temp_time = 2*removed_num + installed_num
    if temp_time <= count:
        count = temp_time
        i_main = i

print(count, i_main)