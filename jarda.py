

def jarda(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return jarda(n-1) + jarda(n-2)


n = int(input())
print(jarda(n))

