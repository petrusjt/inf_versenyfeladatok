

def jarda(n):
    tmp = [0,1]
    for i in range(n):
        (tmp[0], tmp[1]) = (tmp[1], tmp[0] + tmp[1])
        
    
    return tmp[1]



n = int(input())
print(jarda(n))