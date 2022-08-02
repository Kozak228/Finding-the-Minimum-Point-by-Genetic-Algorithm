from numpy import array, append, dot

def poisk_point_2_dot(koordinate, P_2):
    if isinstance(koordinate, dict):
        spisok_koordinate = array([])

        for i in koordinate.values():
            for j in i:
                spisok_koordinate = append(spisok_koordinate, j)
    else:
        spisok_koordinate = array(koordinate)

    # рядок у стовпець
    spisok_koordinate = spisok_koordinate.reshape(-1, 1)
    
    B_D = dot(P_2, spisok_koordinate)
    B = [B_D[0][0], B_D[1][0]]
    D = [B_D[2][0], B_D[3][0]]
 
    return B, D

def poisk_point_4_dot(koordinate, P_2, P_alpha):
    if isinstance(koordinate, dict):
        spisok_koordinate = array([])

        for i in koordinate.values():
            for j in i:
                spisok_koordinate = append(spisok_koordinate, j)
    else:
        spisok_koordinate = array(koordinate)

    spisok_koordinate = spisok_koordinate.reshape(-1, 1)
    
    A_C = dot(P_alpha, spisok_koordinate)
    A = [A_C[0][0], A_C[1][0]]
    C = [A_C[2][0], A_C[3][0]]

    B_D_1 = dot(P_alpha, spisok_koordinate)
    B_D = dot(P_2, B_D_1)

    B = [B_D[0][0], B_D[1][0]]
    D = [B_D[2][0], B_D[3][0]]
 
    return A, C, B, D

def dot_in_Serpinskiy(koord, P_div):
    spisok_koordinate = koord.reshape(-1, 1)
    
    point = dot(P_div, spisok_koordinate)
    
    X = [point[0][0], point[1][0]]

    return X

def dot_atract(spisok, P_atract_1, P_atract_2):
    sp = array([])

    for i in spisok:
        for j in i:
            sp = append(sp, j)

    sp = sp.reshape(-1, 1)

    A = dot(P_atract_1, sp)
    B = dot(P_atract_2, sp)

    s1 = [A[0][0], A[1][0]]
    s2 = [A[2][0], A[3][0]]
    s3 = [B[0][0], B[1][0]]
    s4 = [B[2][0], B[3][0]]
    
    return s1, s2, s3, s4

def new_point(spisok, P_a, Q_b):
    spisok_one, spisok_two = array([]), array([])

    for i in range(len(spisok)):
        if i < 2:
            for j in spisok[i]:
                spisok_one = append(spisok_one, j)
        else:
            for j in spisok[i]:
                spisok_two = append(spisok_two, j)

    spisok_one = spisok_one.reshape(-1, 1)
    spisok_two = spisok_two.reshape(-1, 1)

    A = dot(P_a, spisok_one)
    C = dot(P_a, spisok_two)
    B = dot(Q_b, spisok_one)
    D = dot(Q_b, spisok_two)

    a = [A[0][0], A[1][0]]
    a1 = [A[2][0], A[3][0]]
    c = [B[0][0], B[1][0]]
    c1 = [B[2][0], B[3][0]]
    b = [C[0][0], C[1][0]]
    b1 = [C[2][0], C[3][0]]
    d = [D[0][0], D[1][0]]
    d1 = [D[2][0], D[3][0]]
    
    return a, a1, c, c1, b, b1, d, d1

def poisk_point_z(koordinate, P_2):
    spisok_koordinate_one = array([])

    for i in koordinate:
        for j in i:
            spisok_koordinate_one = append(spisok_koordinate_one, j)

    spisok_koordinate_one = spisok_koordinate_one.reshape(-1, 1)
    
    A_C = dot(P_2, spisok_koordinate_one)

    A = [A_C[0][0], A_C[1][0]]
    C = [A_C[2][0], A_C[3][0]]
 
    return A, C