from matplotlib.pyplot import subplots, show, plot, pause, savefig

from Sorted import sort_dict
from Granich_draw import granich_draw_cross
from Proverka import proverka_path

class Draw:
    def __init__(self):
        self.spisok_dirs = ["Основний алгоритм", "Вибір певної популяції", "Рух точки мінімуму"]

    def draw_genetic(self, ax, spisok, cnt_genetic, mut):
        path_dir = proverka_path(self.spisok_dirs[0])

        ax.clear()
        ax.set_title(f"Покоління: {cnt_genetic}.")

        if mut == False and len(spisok) == 2:
            stor, min_dot = spisok

            spis_x = [i[0] for i in stor.values()]
            spis_y = [i[1] for i in stor.values()]

            spis_x.sort()
            spis_y.sort()

            min_dot_for_granich_x, max_dot_for_granich_x = granich_draw_cross(spis_x[0], spis_x[-1]) 
            min_dot_for_granich_y, max_dot_for_granich_y = granich_draw_cross(spis_y[0], spis_y[-1])

            ax.set_xlim(min_dot_for_granich_x, max_dot_for_granich_x)
            ax.set_ylim(min_dot_for_granich_y, max_dot_for_granich_y)

            stor = sort_dict(stor)

            spisok_dot = [i for i in stor.values()]

            spisok_dot.append(stor.get("A"))

            draw_line = []

            for i in spisok_dot:
                draw_line.append(i)
                plot(*zip(*draw_line), linewidth=2, color="blue")
                pause(1)

            ax.scatter(*zip(min_dot), marker="X", color='red', zorder=5)
            pause(1)

            savefig(f"{path_dir}Osn_alg_{cnt_genetic}_crossin.png")

        else:
            storoni_pryamoygol_mal, storoni_pryamoygol, spisok_dot_mut, min_dot = spisok[0], spisok[1], spisok[2], spisok[3]

            spis_stor = [i for i in storoni_pryamoygol.values()]
            spis_x = [i[0] for i in spis_stor[:4]]
            spis_y = [i[1] for i in spis_stor[:4]]
            
            spis_x.sort()
            spis_y.sort()

            ax.set_xlim(spis_x[0] - 4, spis_x[-1] + 4)
            ax.set_ylim(spis_y[0] - 4, spis_y[-1] + 4)
    
            storoni_pryamoygol = sort_dict(storoni_pryamoygol)
            storoni_pryamoygol_mal = sort_dict(storoni_pryamoygol_mal)

            draw_dot = [i for i in storoni_pryamoygol.values()]

            for i in storoni_pryamoygol_mal.values():
                draw_dot.append(i)

            draw_line_all = [i for i in storoni_pryamoygol.values()]
            draw_line = [i for i in draw_line_all[:4]]

            draw_line_mal = [i for i in storoni_pryamoygol_mal.values()]

            draw_line.append(storoni_pryamoygol.get("A"))
            draw_line_mal.append(storoni_pryamoygol_mal.get("A1"))

            draw_dot1, draw_line_1, draw_line_mal_1 = [], [], []

            for i in draw_dot:
                draw_dot1.append(i)
                ax.scatter(*zip(*draw_dot1), marker='X', color='darkred', zorder=5)
                pause(0.1)

            for i in draw_line:
                draw_line_1.append(i)
                plot(*zip(*draw_line_1), linewidth=2, color="blue")
                pause(0.1)

            for i in draw_line_mal:
                draw_line_mal_1.append(i)
                plot(*zip(*draw_line_mal_1), linewidth=2, color='green')
                pause(0.1)
            
            ax.scatter(*zip(*spisok_dot_mut), color='darkviolet', s=8, zorder=3)
            pause(1)
            ax.scatter(*zip(min_dot), marker="X", color='red', zorder=5)
            pause(1)

            savefig(f"{path_dir}Osn_alg_{cnt_genetic}_mut.png")

    def vybor_popul_min_dot_draw(self, spisok_min_dot, number_of_popul_one, number_of_popul_two):
        path_dir = proverka_path(self.spisok_dirs[2])

        spis_x = [i[0] for i in spisok_min_dot]
        spis_y = [i[1] for i in spisok_min_dot]

        fig, ax = subplots()

        if number_of_popul_one == number_of_popul_two:
            ax.set_title(f"Покоління: {number_of_popul_one}.")
        else:
            ax.set_title(f"Покоління: {number_of_popul_one} - {number_of_popul_two}.")

        ax.set_xlim(min(spis_x) - 1, max(spis_x) + 1)
        ax.set_ylim(min(spis_y) - 1, max(spis_y) + 1)

        spisok_min_dot_draw = []

        for i in spisok_min_dot:
            spisok_min_dot_draw.append(i)

            plot(*zip(*spisok_min_dot_draw), linewidth=1, color="blue")
            ax.scatter(*zip(*spisok_min_dot_draw), marker="X", color="red", zorder=5)
            pause(1)
        
        savefig(f"{path_dir}low_point_movement.png")
        show()

    def vybor_popul_draw(self, ax, storoni_pryamoygol, min_dot, crossing, number_of_popul_one, number_of_popul_two, storoni_pryamoygol_mal = {}, spisok_dot_mut = []):
        path_dir = proverka_path(self.spisok_dirs[1])
        
        if number_of_popul_one == number_of_popul_two:
            ax.set_title(f"Покоління: {number_of_popul_one}.")
        else:
            ax.set_title(f"Покоління: {number_of_popul_one} - {number_of_popul_two}.")

        if crossing:
            storoni_pryamoygol = sort_dict(storoni_pryamoygol)

            spisok_dot = [i for i in storoni_pryamoygol.values()]
            spisok_dot.append(storoni_pryamoygol.get("A"))

            draw_line = []
            for i in spisok_dot:
                draw_line.append(i)
                plot(*zip(*draw_line), linewidth=2, color="blue")
                pause(1)

            ax.scatter(*zip(min_dot), marker="X", color='red', zorder=5)
            pause(1)

        else:    
            storoni_pryamoygol = sort_dict(storoni_pryamoygol)
            storoni_pryamoygol_mal = sort_dict(storoni_pryamoygol_mal)

            draw_dot = [i for i in storoni_pryamoygol.values()]

            for i in storoni_pryamoygol_mal.values():
                draw_dot.append(i)

            draw_line_all = [i for i in storoni_pryamoygol.values()]
            draw_line = [i for i in draw_line_all[:4]]

            draw_line_mal = [i for i in storoni_pryamoygol_mal.values()]

            draw_line.append(storoni_pryamoygol.get("A"))
            draw_line_mal.append(storoni_pryamoygol_mal.get("A1"))

            draw_dot1, draw_line_1, draw_line_mal_1 = [], [], []

            for i in draw_dot:
                draw_dot1.append(i)
                ax.scatter(*zip(*draw_dot1), marker='X', color='darkred', zorder=5)
                pause(0.1)

            for i in draw_line:
                draw_line_1.append(i)
                plot(*zip(*draw_line_1), linewidth=2, color="yellow")
                pause(0.1)

            for i in draw_line_mal:
                draw_line_mal_1.append(i)
                plot(*zip(*draw_line_mal_1), linewidth=2, color='green')
                pause(0.1)
            
            ax.scatter(*zip(*spisok_dot_mut), color='darkviolet', s=8, zorder=3)
            pause(1)
            ax.scatter(*zip(min_dot), marker="X", color='red', zorder=5)
            pause(1)
            
        savefig(f"{path_dir}certain_population.png")