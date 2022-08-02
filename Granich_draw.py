def granich_draw_cross(min_dot, max_dot):
    koor_min, koor_max = 0.0, 0.0

    if -1 >= min_dot or min_dot >= 1:
        koor_min = min_dot - 1
    elif -0.5 >= min_dot or min_dot >= 0.5:
        koor_min = min_dot - 0.1
    elif -0.1 >= min_dot or min_dot >= 0.1:
        koor_min = min_dot - 0.01
    elif -0.01 >= min_dot or min_dot >= 0.01:
        koor_min = min_dot - 0.001
    else:
        koor_min = min_dot - 0.0001
        
    if 1 <= max_dot or max_dot <= -1:
        koor_max = max_dot + 1
    elif 0.5 <= max_dot or max_dot <= -0.5:
        koor_max = max_dot + 0.1
    elif 0.1 <= max_dot or max_dot <= -0.1:
        koor_max = max_dot + 0.01
    elif 0.01 <= max_dot or max_dot <= -0.01:
        koor_max = max_dot + 0.001
    else:
        koor_max = max_dot + 0.0001

    return koor_min, koor_max


def granich_dot_z(x, x2, y, y2):
    if x2 <= 0 and y2 <= 0:
        return x, x2 + 1, y, y2 + 1
    else:
        return x - 0.1, x2 + 0.1, y - 0.1, y2 + 0.1