already_calculated = {1 : 1, 2 : 2}

def jarda2(n):
    if n in already_calculated:
        return already_calculated[n]
    else:
        already_calculated[n] = jarda2(n-1) + jarda2(n-2)
        return already_calculated[n]

n = int(input())
print(jarda2(n))