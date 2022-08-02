from Draw import Draw
from numpy import array, append, random
from random import uniform
from math import fabs, sqrt, pow
from time import sleep

from P_and_Q_matrix_and_other_matrix import p_and_q_matrix_and_other_matrix
from Functions_for_genetic import poisk_point_2_dot, poisk_point_4_dot, dot_in_Serpinskiy, dot_atract, new_point, poisk_point_z
from Sorted import selection_sort
from Granich_draw import granich_dot_z

class Genetic:
    def __init__(self, a, c, Rand_chisl_for_P_Q, function, function_str):
        self.a = a
        self.c = c
        self.func = function
        self.func_str = function_str
        self.P_2, self.P_a, self.Q_b, self.P_alpha, self.P_Serpir, self.P_atract_1, self.P_atract_2 = p_and_q_matrix_and_other_matrix(Rand_chisl_for_P_Q)
        self.draw = Draw()

        self.storoni_pryamoygol_and_minDot_for_one_popul = {}
        
    def crossin(self, a, c):
        storoni_pryamoygol = {}
        storoni_pryamoygol_for_draw = []
        
        storoni_pryamoygol["A"] = a
        storoni_pryamoygol["C"] = c

        storoni_pryamoygol["B"], storoni_pryamoygol["D"] = poisk_point_2_dot(storoni_pryamoygol, self.P_2)

        spis_st = [i for i in storoni_pryamoygol.values()]

        storoni_pryamoygol_for_draw.append(storoni_pryamoygol)

        spisok_new_st = list(new_point(spis_st, self.P_a, self.Q_b))
        
        spisok_new_st_znach = [self.func(i, self.func_str) for i in spisok_new_st]

        spis_with_z_k = [spisok_new_st[spisok_new_st_znach.index(min(spisok_new_st_znach))]]
    
        for i in spis_st:
            l = 0
            storoni_pryamoygol_for_z = {}

            storoni_pryamoygol_for_z[l] = i
            storoni_pryamoygol_for_z[l + 1] = spis_with_z_k[0]

            storoni_pryamoygol_for_z[l + 2], storoni_pryamoygol_for_z[l + 3] = poisk_point_2_dot(storoni_pryamoygol_for_z, self.P_2)

            spis_new = [i for i in storoni_pryamoygol_for_z.values()]

            spisok_new_st = list(new_point(spis_new, self.P_a, self.Q_b))

            spisok_new_st_znach = [self.func(i, self.func_str) for i in spisok_new_st]
            
            spis_with_z_k.append(spisok_new_st[spisok_new_st_znach.index(min(spisok_new_st_znach))])
        
        spis_with_z_k_zhach = [self.func(i, self.func_str) for i in spis_with_z_k]

        selection_sort(spis_with_z_k_zhach, spis_with_z_k)

        storoni_pryamoygol_1 = list(poisk_point_z(spis_with_z_k[:2], self.P_alpha))

        func_zh = [self.func(i, self.func_str) for i in storoni_pryamoygol_1]

        return storoni_pryamoygol_1, func_zh, storoni_pryamoygol_for_draw  
    
    def mutations(self, a, c, cnt_dot_in_Serp):
        storoni_pryamoygol, storoni_pryamoygol_mal, = {}, {}
        storoni_two_pryamoygols_and_dot_mut = []
        
        storoni_pryamoygol_mal["A1"] = a
        storoni_pryamoygol_mal["C1"] = c
        
        spis_for_poisk_dot_z = [a, c]

        storoni_pryamoygol["A"], storoni_pryamoygol["C"], storoni_pryamoygol["B"], storoni_pryamoygol["D"] = poisk_point_4_dot(storoni_pryamoygol_mal, self.P_2, self.P_alpha)

        spis_for_poisk_dot_z.append(storoni_pryamoygol.get("A"))
        spis_for_poisk_dot_z.append(storoni_pryamoygol.get("C"))

        storoni_pryamoygol_mal["B1"], storoni_pryamoygol_mal["D1"] = poisk_point_2_dot(storoni_pryamoygol_mal, self.P_2)

        poisk_blizh_stor = [i for i in storoni_pryamoygol_mal.values()]
    
        storoni_two_pryamoygols_and_dot_mut.append(storoni_pryamoygol_mal)

        spis_storoni_pryamoygol = [i for i in storoni_pryamoygol_mal.values()]

        # Атракторы
        storoni_pryamoygol["E"], storoni_pryamoygol["F"], storoni_pryamoygol["G"], storoni_pryamoygol["H"] = dot_atract(spis_storoni_pryamoygol[:2], self.P_atract_1, self.P_atract_2)

        storoni_two_pryamoygols_and_dot_mut.append(storoni_pryamoygol)

        spisok_storon = [i for i in storoni_pryamoygol.keys()]

        spisok_dot = []

        spis_dot_x = [i[0] for i in spis_for_poisk_dot_z]
        spis_dot_y = [i[1] for i in spis_for_poisk_dot_z]

        spis_dot_x.sort()
        spis_dot_y.sort()
        
        x, x2, y, y2 = granich_dot_z(spis_dot_x[0], spis_dot_x[-1], spis_dot_y[0], spis_dot_y[-1]) 

        z = [uniform(x, x2), uniform(y, y2)]

        for _ in range(cnt_dot_in_Serp):
            spisok_kordinate = array([])
            
            for i in z:
                spisok_kordinate = append(spisok_kordinate, i)

            for i in storoni_pryamoygol.get(random.choice(spisok_storon)):
                spisok_kordinate = append(spisok_kordinate, i)

            z = dot_in_Serpinskiy(spisok_kordinate, self.P_Serpir)
            spisok_dot.append(z)

        storoni_two_pryamoygols_and_dot_mut.append(spisok_dot)

        spisok_dot_zh = [self.func(i, self.func_str) for i in spisok_dot]

        selection_sort(spisok_dot_zh, spisok_dot)

        min_dot = spisok_dot[0]

        storoni_two_pryamoygols_and_dot_mut.append(min_dot)

        distance_between_stor_and_minDot = []

        for i in poisk_blizh_stor:
            distance_between_stor_and_minDot.append(sqrt(pow(i[0] - min_dot[0], 2) + pow(i[1] - min_dot[1], 2)))

        selection_sort(distance_between_stor_and_minDot, poisk_blizh_stor)

        return storoni_two_pryamoygols_and_dot_mut, poisk_blizh_stor[0]

    def vybor_population_min_dot(self, number_of_popul_one, number_of_popul_two):
        spisok_min_dot = [self.storoni_pryamoygol_and_minDot_for_one_popul.get(i)[-1] for i in range(number_of_popul_one, number_of_popul_two + 1)]

        self.draw.vybor_popul_min_dot_draw(spisok_min_dot, number_of_popul_one, number_of_popul_two)

    def vybor_population(self, ax, number_of_popul_one, number_of_popul_two):
        all_storoni = []

        for i in range(number_of_popul_one, number_of_popul_two + 1):
            if len(self.storoni_pryamoygol_and_minDot_for_one_popul.get(i)) == 2:
                for i in self.storoni_pryamoygol_and_minDot_for_one_popul.get(i)[0].values():
                    all_storoni.append(i)
            else:
                for i in self.storoni_pryamoygol_and_minDot_for_one_popul.get(i)[1].values():
                    all_storoni.append(i)

            
        spis_x = [i[0] for i in all_storoni]
        spis_y = [i[1] for i in all_storoni]

        spis_x.sort()
        spis_y.sort()
        
        ax.set_xlim(spis_x[0] - 2, spis_x[-1] + 2)
        ax.set_ylim(spis_y[0] - 2, spis_y[-1] + 2)

        for i in range(number_of_popul_one, number_of_popul_two + 1):
            if len(self.storoni_pryamoygol_and_minDot_for_one_popul.get(i)) == 2:
                storoni_pryamoygol, min_dot = self.storoni_pryamoygol_and_minDot_for_one_popul.get(i)
                self.draw.vybor_popul_draw(ax, storoni_pryamoygol, min_dot, True, number_of_popul_one, number_of_popul_two)

            else:
                storoni_pryamoygol_mal, storoni_pryamoygol, spisok_dot_mut, min_dot = self.storoni_pryamoygol_and_minDot_for_one_popul.get(i)
                self.draw.vybor_popul_draw(ax, storoni_pryamoygol, min_dot, False, number_of_popul_one, number_of_popul_two, storoni_pryamoygol_mal, spisok_dot_mut)
                
    def start_genetic(self, ax, pohib, cnt_dot_in_Serp):
        cnt_mutation = 0
        mutations_on, algorithms_off = False, False
        
        for cnt_genetic in range(1, 20000):
            mutations = False

            dot_squere_one_and_tree, dot_squere_one_and_tree_zhnach, storoni_pryamoygol_and_minDot = self.crossin(self.a, self.c) 

            a1 = storoni_pryamoygol_and_minDot[0].get("A")
            b1 = storoni_pryamoygol_and_minDot[0].get("B")
            c1 = storoni_pryamoygol_and_minDot[0].get("C")
            d1 = storoni_pryamoygol_and_minDot[0].get("D")

            if a1 == b1 or c1 == d1 or (a1[0] == b1[0] == c1[0] == d1[0]) or (a1[1] == b1[1] == c1[1] == d1[1]):
                mutations_on = True

            else:
                if dot_squere_one_and_tree_zhnach[1] > dot_squere_one_and_tree_zhnach[0]:
                    min_dot, a = dot_squere_one_and_tree
                else:
                    a, min_dot = dot_squere_one_and_tree

                storoni_pryamoygol_and_minDot.append(min_dot)

                obshiy_storoni_pryamoygol_and_minDot = storoni_pryamoygol_and_minDot

            if self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic - 1) != None:
                if self.func(self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic - 1)[-1], self.func_str) <= self.func(obshiy_storoni_pryamoygol_and_minDot[-1], self.func_str) or mutations_on:
                    chetchik = 0

                    while True:
                        if chetchik >= 5:
                            break

                        storoni_two_pryamoygol_and_dot_mut, a = self.mutations(self.a, self.c, cnt_dot_in_Serp)

                        storoni_pryamoygol_and_minDot = storoni_two_pryamoygol_and_dot_mut
                        
                        if self.func(storoni_two_pryamoygol_and_dot_mut[-1], self.func_str) < self.func(self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic - 1)[-1], self.func_str):
                            min_dot = storoni_two_pryamoygol_and_dot_mut[-1]

                            obshiy_storoni_pryamoygol_and_minDot = storoni_pryamoygol_and_minDot
                            mutations = True
                            mutations_on = False
                            cnt_mutation += 1
                            break
                        
                        chetchik += 1

            c = [2 * min_dot[0] - a[0], 2 * min_dot[1] - a[1]]

            self.storoni_pryamoygol_and_minDot_for_one_popul[cnt_genetic] = obshiy_storoni_pryamoygol_and_minDot

            if mutations:
                self.draw.draw_genetic(ax, self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic), cnt_genetic, mutations)
            else:
                self.draw.draw_genetic(ax, self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic), cnt_genetic, mutations)

            sleep(1)

            self.a, self.c = a, c      

            if self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic - 1) != None:
                if fabs(sqrt(pow(self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic - 1)[-1][0] - self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic)[-1][0], 2) + \
                             pow(self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic - 1)[-1][1] - self.storoni_pryamoygol_and_minDot_for_one_popul.get(cnt_genetic)[-1][1], 2))) < pohib:
                    algorithms_off = True
                    break

        if algorithms_off:
            return "Алгоритм завершив свою роботу!\nЗакрийте вікно з малюнком", cnt_genetic, cnt_mutation 