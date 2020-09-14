already_calculated = {1 : 1, 2 : 2, 3 : 4}

def jarda3(n):
    if n in already_calculated:
        return already_calculated[n]
    else:
        already_calculated[n] = jarda3(n-1) + jarda3(n-2) + jarda3(n-3)
        return already_calculated[n]

n = int(input())
print(jarda3(n))