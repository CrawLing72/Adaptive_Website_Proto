import sys

K, N = map(int, input().split())
k_list = [int(sys.stdin.readline().strip("\n")) for i in range(K)]
k_list.sort()
k_min = k_list[0]

def check_prob():
    global k_min
    K_list = k_list.copy()
    stacked_len = 0
    while len(K_list) != 0:
        before_len = len(K_list)
        K_list = [t - k_min for t in K_list if t - k_min > 0]
        after_len = len(K_list)
        stacked_len += before_len - after_len
    else:
        k_min -= 1
        return stacked_len

while True:
    predicted_num = check_prob()
    if predicted_num + K == N:
        print(k_min)
        break

