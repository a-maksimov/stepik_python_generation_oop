# put your python code here

n = int(input())


def darts(n):
    row = [1 for _ in range(n)]

    def run(row, counter=1):
        if row == [1]:
            return row

        if counter > n // 2:
            if n % 2 == 0:
                return row
            else:
                print(*row)
                return row

        print(*row)

        row[counter:n - counter] = [counter + 1 for _ in range(n - counter * 2)]
        counter += 1
        new_row = run(row.copy(), counter)

        if new_row != row:
            print(*row)

    run(row.copy())
    print(*row)

darts(n)

# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print(min(i + 1, j + 1, n - i, n - j), end=' ')
#     print()
