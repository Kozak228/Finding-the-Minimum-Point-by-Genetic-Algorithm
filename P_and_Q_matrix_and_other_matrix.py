from numpy import array, zeros

def p_and_q_matrix_and_other_matrix(Rand_P_and_Q):
    P_2 = array([[1, 0, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0],
                 [0, 1, 0, 0]])

    P_Serpir = array([[1/3, 0, 2/3, 0],
                      [0, 1/3, 0, 2/3],
                      [2/3, 0, 1/3, 0],
                      [0, 2/3, 0, 1/3]])

    P_alpha = array([[2, 0, -1, 0],
                     [0, 2, 0, -1],
                     [-1, 0, 2, 0],
                     [0, -1, 0, 2]])

    P_atract_1 = array([[2, 0, -1, 0],
                        [0, 0.5, 0, 0.5],
                        [-1, 0, 2, 0],
                        [0, 0.5, 0, 0.5]])

    P_atract_2 = array([[0.5, 0, 0.5, 0],
                        [0, 2, 0, -1],
                        [0.5, 0, 0.5, 0],
                        [0, -1, 0, 2]])

    P_a = zeros((4, 4))
    Q_b = zeros((4, 4))

    k = 0
    for i in range(len(P_a)):
        if k == 2:
            k = 0
        for j in range(len(P_a[i])):
            if i == j:
                P_a[i][j] = Rand_P_and_Q[k]
                k += 1
    
    for i in range(len(P_a)):
        if k == 4:
            k = 2
        Q_b[i][len(P_a) - i - 1] = Rand_P_and_Q[k]
        k += 1

    for i in range(len(P_a)):
        for j in range(len(P_a[i])):
            if (i == 0 and j == 2) or (i == 2 and j == 0):
                P_a[i][j] = 1 - P_a[0][0]             
            elif (i == 1 and j == 3) or (i == 3 and j == 1):
                P_a[i][j] = 1 - P_a[1][1]
    
    for i in range(len(Q_b)):
        for j in range(len(Q_b[i])):
            if (i == 0 and j == 1) or (i == 2 and j == 3):
                Q_b[i][j] = 1 - Q_b[0][3]             
            elif (i == 1 and j == 0) or (i == 3 and j == 2):
                Q_b[i][j] = 1 - Q_b[1][2]

    return P_2, P_a, Q_b, P_alpha, P_Serpir, P_atract_1, P_atract_2