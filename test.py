T = int(input())


for i in range(T):

    a = list(map(int, input().split()))
    result = [num for num in a if num % 2 == 1]
    print(f'#{i+1} {sum(result)}')
