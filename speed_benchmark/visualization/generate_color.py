import colorsys
import random


def get_n_hls_colors(num):
    hls_colors = []
    for i in range(num):
        h_item = i / num
        s_item = 0.9 + random.random() * 0.1
        l_item = 0.5 + random.random() * 0.1
        hls_colors.append([h_item, l_item, s_item])
    return hls_colors


def ncolors(num):
    if num < 1:
        return []
    return [colorsys.hls_to_rgb(*hlsc) for hlsc in get_n_hls_colors(num)]
