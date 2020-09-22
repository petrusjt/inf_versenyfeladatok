# T - utolsó 1 egység hossz
# A - alsó fűrészfog
# F - felső fűrészfog

# T_N = 2*T_{N-1} + T_{N-2} + A_N + F_N, ha N > 2

# A_N = F_{N-1} + T_{N-1}
# F_N = A_{N-1} + T_{N-1}

# A_1 = F_1 = 1

# T_1 = 2
# T_2 = 7
# //T_3 = 22

# T_N = 2T_{N-1} + T_{N-2} + 2A_{N-1}
# A_N = A_{N-1} + T_{N-1}

# T_N = 3*T_{N-1} + T_{N-2} - T_{N-3}

already_calculated = {1 : 2, 2 : 7, 3 : 22}


def jarda2(N):
    if N in already_calculated:
        return already_calculated[N]
    else:
        already_calculated[N] = 3 * jarda2(N-1) + jarda2(N-2) - jarda2(N-3)
        return already_calculated[N]


print(jarda2(int(input())))
