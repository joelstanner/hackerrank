size = int(input())
arr = [int(x) for x in input().split()]
e = arr.pop()

def main(size, arr, e):
    for i in range(size - 2, -1, -1):
        if arr[i] > e:
            try:
                arr[i + 1] = arr[i]
                print(*arr)
            except IndexError:
                arr.append(arr[i])
                print(*arr)
        else:
            try:
                arr[i + 1] = e
            except IndexError:
                arr.append(e)
            finally:
                print(*arr)
                break
    else:
        arr[0] = e
        print(*arr)

if __name__ == '__main__':
    main(size, arr, e)
