T = int(input())

month_12 = ['0'+str(x) for x in range(1, 10)]
month_12 += ['10', '11', '12']

for t in range(T):
    calendar = input()
    year, month, days = calendar[0:4], calendar[4:6], calendar[6:8]

    if month in month_12:
        if month == '02':
            if int(days) > 0 and int(days) <= 28:
                print('#{} {}/{}/{}'.format(t+1, year, month, days))
            else:
                print('#{} {}'.format(t+1, -1))
        elif month in ['04', '06', '09', '11']:
            if int(days) > 0 and int(days) <= 30:
                print('#{} {}/{}/{}'.format(t+1, year, month, days))
            else:
                print('#{} {}'.format(t+1, -1))
        else:
            if int(days) > 0 and int(days) <= 31:
                print('#{} {}/{}/{}'.format(t+1, year, month, days))
            else:
                print('#{} {}'.format(t+1, -1))
    else:
        print('#{} {}'.format(t+1, -1))
