def sort_dict(dicts):
    sorted_tuple = sorted(dicts.items(), key=lambda x: x[0])
    return dict(sorted_tuple)

def selection_sort(spis_znach, spis_dot):
	for i in range(len(spis_znach)):
		minn = i
		for j in range(i + 1, len(spis_znach)):
			if spis_znach[j] < spis_znach[minn]:
				minn = j
		spis_znach[i], spis_znach[minn] = spis_znach[minn], spis_znach[i]
		spis_dot[i], spis_dot[minn] = spis_dot[minn], spis_dot[i]